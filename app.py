from flask import Flask, render_template, request, redirect, url_for, flash, g
import sqlite3
import os
from pathlib import Path

# Create the Flask app instance.
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")

# Keep database path near this file so beginners can find it easily.
BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "notes.db"


def get_db():
    """Get a database connection for the current request."""
    if "db" not in g:
        # sqlite3.Row lets us access columns by name, e.g., row["title"].
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


def init_db():
    """Create the notes table if it does not already exist."""
    db = get_db()
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.commit()


@app.teardown_appcontext
def close_db(exception):
    """Close the database connection when the request ends."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    """Show all notes on the home page."""
    db = get_db()
    notes = db.execute(
        "SELECT id, title, content, created_date FROM notes ORDER BY created_date DESC"
    ).fetchall()
    return render_template("index.html", notes=notes)


@app.route("/add", methods=["GET", "POST"])
def add_note():
    """Create a new note."""
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        # Basic validation to keep entries meaningful.
        if not title or not content:
            flash("Title and content are required.", "danger")
            return render_template("add_note.html", title=title, content=content)

        db = get_db()
        db.execute(
            "INSERT INTO notes (title, content) VALUES (?, ?)",
            (title, content),
        )
        db.commit()
        flash("Note added successfully.", "success")
        return redirect(url_for("index"))

    return render_template("add_note.html")


@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    """Edit an existing note by its ID."""
    db = get_db()
    note = db.execute(
        "SELECT id, title, content, created_date FROM notes WHERE id = ?",
        (note_id,),
    ).fetchone()

    if note is None:
        return render_template("404.html"), 404

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        if not title or not content:
            flash("Title and content are required.", "danger")
            return render_template("edit_note.html", note=note)

        db.execute(
            "UPDATE notes SET title = ?, content = ? WHERE id = ?",
            (title, content, note_id),
        )
        db.commit()
        flash("Note updated successfully.", "success")
        return redirect(url_for("index"))

    return render_template("edit_note.html", note=note)


@app.route("/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    """Delete a note by ID."""
    db = get_db()
    result = db.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    db.commit()

    if result.rowcount == 0:
        flash("Note not found.", "warning")
    else:
        flash("Note deleted successfully.", "info")

    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(error):
    """Render a friendly 404 page."""
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    """Render a friendly 500 error page."""
    return render_template("500.html"), 500


# Initialize the database table at startup.
with app.app_context():
    init_db()


if __name__ == "__main__":
    # debug=True is beginner-friendly for local development.
    app.run(debug=True)

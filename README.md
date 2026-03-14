# Flask Notes Web App 📝

A **beginner-friendly** Notes application built with **Python Flask**. Create, read, update, and delete notes with a clean, responsive **Bootstrap 5** UI and **SQLite** database.

Perfect for learning Flask fundamentals with a real, functional project!

## ✨ Features

✅ **Create Notes** - Add new notes with title and content
✅ **View Notes** - Display all notes on the home page in card layout
✅ **Edit Notes** - Update existing notes with ease
✅ **Delete Notes** - Remove notes you no longer need
✅ **Responsive Design** - Works beautifully on desktop, tablet, and mobile
✅ **Flash Messages** - User-friendly notifications for all actions
✅ **Clean UI** - Built with Bootstrap 5 and custom CSS
✅ **Error Handling** - Custom 404 and 500 error pages
✅ **Production-Ready** - Configured for Heroku and Vercel deployment

## 🛠️ Tech Stack

- **Backend:** Python Flask
- **Database:** SQLite (zero-setup, file-based)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Icons:** Bootstrap Icons
- **Deployment:** Heroku, Vercel

## 📁 Project Structure

```
notes.flask/
├── app.py                    # Main Flask application with all routes
├── requirements.txt          # Python dependencies
├── Procfile                  # Heroku deployment config
├── runtime.txt              # Python version for Heroku
├── vercel.json              # Vercel deployment config
├── .gitignore               # Git ignore file
├── README.md                # This file
├── notes.db                 # SQLite database (auto-created)
├── templates/               # HTML templates folder
│   ├── base.html            # Base template with navbar layout
│   ├── index.html           # Home page (list all notes)
│   ├── add_note.html        # Add note form page
│   ├── edit_note.html       # Edit note form page
│   ├── 404.html             # 404 error page
│   └── 500.html             # 500 error page
└── static/                  # Static files folder
    └── style.css            # Custom CSS styles (with comments!)
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed on your system
- **pip** (Python package manager) - comes with Python
- (Optional) **Git** for version control

### Step 1: Clone or Download

```bash
# Clone from GitHub
git clone https://github.com/your-username/notes.flask.git
cd notes.flask

# OR download and unzip manually
```

### Step 2: Create Virtual Environment

A virtual environment keeps your project dependencies isolated from your system Python.

**Windows (Command Prompt):**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Your terminal prompt will show `(venv)` when activated.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- **Flask** - Web framework
- **Werkzeug** - WSGI utilities (used by Flask)
- **gunicorn** - Production web server

### Step 4: Run the Application

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 5: Access the App

Open your web browser and go to:

```
http://localhost:5000
```

You'll see the Notes app homepage! 🎉

### Step 6: Deactivate Virtual Environment

When you're done working:

```bash
deactivate
```

## 💡 How to Use the App

### Adding a Note

1. Click **"Add Note"** button in the navigation bar
2. Enter a **title** and **content**
3. Click **"Save Note"**
4. Success message appears, and you're redirected to the home page

### Viewing Notes

- All your notes appear as **cards** on the home page
- Notes are displayed **newest first**
- Each card shows: title, content preview, and creation date

### Editing a Note

1. Find the note you want to edit
2. Click the **"Edit"** button on the card
3. Update the title and/or content
4. Click **"Update Note"**
5. Changes are saved and you return home

### Deleting a Note

1. Click the **"Delete"** button on any note card
2. Confirm when prompted (prevents accidental deletion)
3. The note is permanently removed from the database

## 📚 Code Explanations (For Beginners)

### `app.py` - The Main Application

This is the heart of your Flask app. It contains:

**Database Setup:**
- Creates and connects to `notes.db` (SQLite file)
- Automatically creates the `notes` table on startup
- Stores: id, title, content, created_date

**Routes (URL endpoints):**
- `GET /` → Display all notes
- `GET/POST /add` → Create new note
- `GET/POST /edit/<id>` → Edit existing note
- `POST /delete/<id>` → Delete note

**Each route is commented explaining:**
- What it does
- What HTTP method it accepts
- What it returns
- How database operations work

**Error Handlers:**
- 404 (Page Not Found)
- 500 (Server Error)

### `templates/` - HTML Files

**base.html** (Shared Layout)
- Navigation bar with links
- Bootstrap 5 CSS setup
- Flash message display
- Footer
- All other templates "extend" this file

**index.html** (Home Page)
- Loops through all notes
- Displays each note in a Bootstrap card
- Shows Edit/Delete buttons for each note
- Empty state message when no notes exist

**add_note.html** (Create Form)
- Form with title and content fields
- Sends data via POST to `/add`
- Cancel button to go back

**edit_note.html** (Edit Form)
- Same form as add_note.html
- Pre-fills with existing note data
- Sends data via POST to `/edit/<id>`

**404.html & 500.html** (Error Pages)
- User-friendly error messages
- Button to return home

### `static/style.css` - Custom Styling

All CSS is **heavily commented** to teach you:

- How to style cards with hover effects
- Responsive design for mobile/tablet/desktop
- Form styling and focus states
- Button styling and transitions
- Dark mode support (CSS only, future enhancement)
- Accessibility best practices

### `requirements.txt` - Dependencies

Lists all Python packages needed:
```
Flask==3.1.0         # Web framework
Werkzeug==3.0.0      # WSGI utilities
gunicorn==21.2.0     # Production server
```

### Configuration Files

**Procfile**
- Tells Heroku how to start the app
- `web: gunicorn app:app`

**runtime.txt**
- Specifies Python version for Heroku
- `python-3.11.0`

**vercel.json**
- Configures Vercel deployment
- Routes all requests to Flask app

**.gitignore**
- Tells Git what files to ignore
- Excludes: `__pycache__/`, `venv/`, `*.db`, `.env`

## 🌐 Deployment to Heroku

Heroku is a free platform to host Python web apps. Your app will be live on the internet!

### Prerequisites
- Heroku account (sign up at heroku.com - free tier available!)
- Heroku CLI installed
- Git repository initialized

### Deployment Steps

1. **Install Heroku CLI**
   - Download from: https://devcenter.heroku.com/articles/heroku-cli

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Initialize Git (if not done)**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Flask Notes app"
   ```

4. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

5. **Deploy to Heroku**
   ```bash
   git push heroku main
   ```

6. **View Your App**
   ```bash
   heroku open
   ```

Your app is now live at: `https://your-app-name.herokuapp.com` 🚀

## 🌐 Deployment to Vercel

Vercel uses the included `vercel.json` configuration.

1. Push code to GitHub
2. Go to vercel.com and click "New Project"
3. Select your GitHub repository
4. Deploy!

Your app will be live at a Vercel URL.

## 📤 Push Code to GitHub

Make your code available on GitHub:

```bash
git init
git add .
git commit -m "Initial commit: Flask Notes app"
git branch -M main
git remote add origin https://github.com/your-username/notes.flask.git
git push -u origin main
```

## 🐛 Troubleshooting

### "Address already in use" Error
```bash
python app.py --port 5001
```

### Database File Not Found
Run the app once to auto-create it:
```bash
python app.py
```

### Template Not Found Error
1. Check `templates/` folder exists
2. Verify template filename spelling
3. Ensure templates are in `templates/` folder

### Bootstrap Not Styling
1. Check internet connection
2. Clear browser cache (Ctrl+Shift+Del)
3. Check browser console (F12)

## 📖 Learning Resources

- **Flask:** https://flask.palletsprojects.com/
- **Bootstrap:** https://getbootstrap.com/docs/5.3/
- **SQLite:** https://www.sqlite.org/docs.html

## 🎨 Next Enhancements

Ideas to improve this project:
- Search functionality
- Categories/Tags
- User accounts with login
- Rich text editor
- Dark mode toggle
- Export notes as PDF
- Cloud backup

## 💻 Code Comments

All code is heavily commented for learning. Start with:
1. `app.py` - Understand the routes
2. `templates/base.html` - Learn template structure
3. `static/style.css` - Study CSS techniques

## 📝 License

Open source and available for educational purposes.

---

**Happy Note-Taking! 📝**

Created with ❤️ for beginners learning Flask Web Development.

# PythonAnywhere Deployment Guide

## Part 1: Push to GitHub

### Step 1: Initialize Git Repository

Open your terminal in the project folder and run:

```bash
git init
git add .
git commit -m "Initial commit - JobberMan application"
```

### Step 2: Create GitHub Repository

1. Go to [github.com](https://github.com) and login
2. Click the "+" icon → "New repository"
3. Name it: `jobberman` (or your choice)
4. **DO NOT** check "Initialize with README" (you already have files)
5. Click "Create repository"

### Step 3: Push to GitHub

Copy the commands from GitHub (they'll look like this):

```bash
git remote add origin https://github.com/YOUR_USERNAME/jobberman.git
git branch -M main
git push -u origin main
```

**Note**: Your .env file won't be pushed (it's in .gitignore for security)

---

## Part 2: Deploy to PythonAnywhere

### Step 1: Sign Up

1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Sign up for a free "Beginner" account
3. Verify your email

### Step 2: Clone Your Repository

1. In PythonAnywhere, go to **"Consoles"** tab
2. Click **"Bash"** to open a terminal
3. Run these commands:

```bash
git clone https://github.com/YOUR_USERNAME/jobberman.git
cd jobberman
```

### Step 3: Create .env File on PythonAnywhere

Since .env wasn't pushed to GitHub, create it manually:

```bash
nano .env
```

Paste this content:
```
SECRET_KEY=37d17883380e7759b136d1e5ebb1d2403e538a2c5c1a11391294844a46728420
FLASK_ENV=production
```

Press `Ctrl+X`, then `Y`, then `Enter` to save.

### Step 4: Install Dependencies

```bash
pip3 install --user -r requirements.txt
```

### Step 5: Create Web App

1. Go to **"Web"** tab
2. Click **"Add a new web app"**
3. Click **"Next"** (for free domain)
4. Select **"Flask"**
5. Select **"Python 3.10"** (or latest available)
6. For path, enter: `/home/YOUR_USERNAME/jobberman/app.py`
7. Click **"Next"**

### Step 6: Configure WSGI File

1. In the Web tab, find **"Code"** section
2. Click on the WSGI configuration file link (e.g., `/var/www/yourname_pythonanywhere_com_wsgi.py`)
3. Delete everything and replace with:

```python
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/YOUR_USERNAME/jobberman'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Load environment variables
from dotenv import load_dotenv
project_folder = os.path.expanduser(project_home)
load_dotenv(os.path.join(project_folder, '.env'))

# Import your Flask app
from app import app as application
```

**Replace YOUR_USERNAME with your actual PythonAnywhere username!**

4. Click **"Save"** (top right)

### Step 7: Set Working Directory

1. Still in the Web tab, find **"Code"** section
2. Set **"Working directory"** to: `/home/YOUR_USERNAME/jobberman`
3. Set **"Source code"** to: `/home/YOUR_USERNAME/jobberman`

### Step 8: Reload Web App

1. Scroll to top of Web tab
2. Click the big green **"Reload"** button
3. Wait 10 seconds

### Step 9: Visit Your Site!

Your app is now live at: `https://YOUR_USERNAME.pythonanywhere.com`

---

## About Your Data Files

### Good News for PythonAnywhere:

✅ **Jobbers.txt** and **Jobber.txt** will persist on PythonAnywhere
✅ User signups will be saved permanently
✅ Files won't be deleted unless you manually delete them

### File Locations:

Your data files are stored at:
- `/home/YOUR_USERNAME/jobberman/Jobbers.txt`
- `/home/YOUR_USERNAME/jobberman/Jobber.txt`
- `/home/YOUR_USERNAME/jobberman/jobs.json`

You can view/edit them in the **"Files"** tab.

---

## Updating Your App

When you make changes locally:

### On Your Computer:
```bash
git add .
git commit -m "Description of changes"
git push
```

### On PythonAnywhere:
1. Go to **"Consoles"** → **"Bash"**
2. Run:
```bash
cd jobberman
git pull
```
3. Go to **"Web"** tab
4. Click **"Reload"**

---

## Troubleshooting

### Error: "Something went wrong"
1. Check the **"Error log"** in Web tab
2. Common issues:
   - Wrong path in WSGI file
   - Missing dependencies
   - Syntax errors in code

### Error: "No module named 'app'"
- Check WSGI file has correct path
- Make sure working directory is set correctly

### Sessions not working
- Make sure .env file exists with SECRET_KEY
- Check WSGI file loads dotenv

### Can't see my changes
- Did you run `git pull` in PythonAnywhere?
- Did you click "Reload" button?

---

## Free Tier Limitations

- ✅ Always-on (no sleeping)
- ✅ 512MB disk space
- ✅ Custom domain not included (use subdomain)
- ✅ HTTPS included
- ⚠️ Limited CPU time per day

---

## Next Steps

1. Test all features on live site
2. Create a test user account
3. Try applying to jobs
4. Share your URL with friends!

Your live URL: `https://YOUR_USERNAME.pythonanywhere.com`

---

## Security Reminder

✅ .env file is NOT in GitHub (protected by .gitignore)
✅ Secret key is secure
✅ Only you can access your PythonAnywhere files

**Never share your .env file or commit it to GitHub!**

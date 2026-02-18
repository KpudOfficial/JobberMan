# Quick Start Guide

## Your Questions Answered:

### 1. Do I need to create .env file?
✅ **Already created!** I made it for you with your secret key.

### 2. Will I lose user data without a database?
❌ **No!** On PythonAnywhere, your text files (Jobbers.txt) persist permanently.
- Files stay even after restarts
- User signups are saved
- Only deleted if you manually delete them

### 3. What's the secret key for?
🔐 It secures your Flask sessions (keeps users logged in safely)

---

## What I Created For You:

1. ✅ `.env` - Contains your secret key (DON'T push to GitHub)
2. ✅ `.gitignore` - Protects .env from being uploaded
3. ✅ `requirements.txt` - Lists all dependencies
4. ✅ Updated `app.py` - Now reads from .env file

---

## Your Secret Key:
```
37d17883380e7759b136d1e5ebb1d2403e538a2c5c1a11391294844a46728420
```
(Already in your .env file)

---

## Next Steps (In Order):

### 1️⃣ Push to GitHub (5 minutes)
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_GITHUB_URL
git push -u origin main
```

### 2️⃣ Deploy to PythonAnywhere (10 minutes)
- Sign up at pythonanywhere.com
- Clone your repo
- Create .env file there (copy from local)
- Set up web app
- Done!

📖 **Full instructions**: See `PYTHONANYWHERE_SETUP.md`

---

## Important Files:

| File | Purpose | Push to GitHub? |
|------|---------|----------------|
| `.env` | Secret key | ❌ NO (in .gitignore) |
| `app.py` | Main app | ✅ YES |
| `requirements.txt` | Dependencies | ✅ YES |
| `Jobbers.txt` | User data | ❌ NO (in .gitignore) |
| `.gitignore` | Protects secrets | ✅ YES |

---

## Data Persistence on PythonAnywhere:

```
Your Files → Stored at: /home/USERNAME/jobberman/
├── Jobbers.txt     ✅ Persists (user signups)
├── Jobber.txt      ✅ Persists (user logins)
├── jobs.json       ✅ Persists (applications)
└── .env            ✅ Persists (secret key)
```

**All files stay permanently unless you delete them!**

---

## Testing Locally First:

Before deploying, test that .env works:

```bash
pip install python-dotenv
python app.py
```

Visit: http://localhost:5000

If it works locally, it'll work on PythonAnywhere!

---

## Quick Commands:

### Local Development:
```bash
python app.py
```

### Push Changes:
```bash
git add .
git commit -m "Your message"
git push
```

### Update on PythonAnywhere:
```bash
cd jobberman
git pull
# Then click "Reload" in Web tab
```

---

## Need Help?

1. Check `PYTHONANYWHERE_SETUP.md` for detailed steps
2. Check PythonAnywhere error logs (Web tab)
3. Make sure .env file exists on PythonAnywhere

---

## Your App Will Be Live At:

`https://YOUR_USERNAME.pythonanywhere.com`

(Replace YOUR_USERNAME with your PythonAnywhere username)

---

Good luck! 🚀

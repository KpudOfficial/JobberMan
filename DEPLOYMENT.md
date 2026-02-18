# Deployment Guide - Render (Free & Easy)

## Why Render?
- ✅ Completely free tier
- ✅ Automatic HTTPS
- ✅ Easy GitHub integration
- ✅ No credit card required
- ✅ Auto-deploys on git push

## Step-by-Step Deployment

### 1. Prepare Your Code

First, make sure you have gunicorn installed:
```bash
pip install gunicorn
pip freeze > requirements.txt
```

### 2. Create GitHub Repository

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### 3. Deploy on Render

1. Go to [render.com](https://render.com) and sign up (use GitHub login)

2. Click "New +" → "Web Service"

3. Connect your GitHub repository

4. Configure the service:
   - **Name**: jobberman (or your choice)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

5. Add Environment Variables:
   - Click "Advanced" → "Add Environment Variable"
   - Key: `SECRET_KEY`
   - Value: Generate a random string (use: `python -c "import secrets; print(secrets.token_hex(32))"`)

6. Click "Create Web Service"

7. Wait 2-3 minutes for deployment

8. Your app will be live at: `https://jobberman.onrender.com`

### 4. Important Notes

**Free Tier Limitations:**
- App sleeps after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds to wake up
- 750 hours/month free (enough for one app)

**Data Persistence:**
- Text files (Jobbers.txt, etc.) will reset on each deployment
- For persistent data, upgrade to use Render's PostgreSQL (also free)

### 5. Upgrade to Database (Optional but Recommended)

To keep user data between deployments:

1. In Render dashboard, create a new PostgreSQL database (free tier available)
2. Update your app to use SQLAlchemy instead of text files
3. Connect database using environment variable

## Alternative: PythonAnywhere (Even Simpler)

If you don't want to use Git:

1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Sign up for free account
3. Go to "Files" tab and upload your project files
4. Go to "Web" tab → "Add a new web app"
5. Choose Flask and Python 3.x
6. Point to your app.py file
7. Done! Your app is live

**PythonAnywhere URL**: `https://yourusername.pythonanywhere.com`

## Troubleshooting

### App won't start
- Check logs in Render dashboard
- Verify requirements.txt has all dependencies
- Ensure gunicorn is in requirements.txt

### Session not working
- Make sure SECRET_KEY environment variable is set
- Check that app.secret_key is reading from environment

### Files not persisting
- This is normal on free hosting
- Upgrade to database for persistent storage

## Next Steps After Deployment

1. Test all features on live site
2. Share your URL with users
3. Monitor logs for errors
4. Consider upgrading to database for production use

## Generate Secret Key

Run this command to generate a secure secret key:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and use it as your SECRET_KEY environment variable.

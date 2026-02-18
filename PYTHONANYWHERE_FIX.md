# PythonAnywhere Fix Guide

## Problem: "Username not found. Please sign up first." after signing up

This happens because the file isn't being written or read correctly on PythonAnywhere.

---

## Solution: Update Your Code on PythonAnywhere

### Step 1: Push Updated Code to GitHub

On your local computer:

```bash
git add .
git commit -m "Fix file path handling for PythonAnywhere"
git push
```

### Step 2: Pull Changes on PythonAnywhere

1. Go to PythonAnywhere → **Consoles** → **Bash**
2. Run:

```bash
cd jobberman
git pull
```

### Step 3: Run Debug Script

Still in the bash console:

```bash
python debug_info.py
```

This will show you:
- Where files are being saved
- If files exist and are readable
- How many users are registered

### Step 4: Check File Permissions

```bash
ls -la Jobbers.txt
```

If the file doesn't exist, create it:

```bash
touch Jobbers.txt
chmod 644 Jobbers.txt
```

### Step 5: Reload Your Web App

1. Go to **Web** tab
2. Click the green **"Reload"** button
3. Wait 10 seconds

### Step 6: Test Again

1. Go to your site: `https://YOUR_USERNAME.pythonanywhere.com`
2. Try signing up with a new username
3. Check if it works

---

## Alternative: Manual File Check

### Check if Jobbers.txt exists:

In PythonAnywhere Bash console:

```bash
cd ~/jobberman
cat Jobbers.txt
```

If it's empty or doesn't exist, that's the problem!

### Manually add a test user:

```bash
echo "(username:testuser,password:testpass)" >> Jobbers.txt
```

Then try logging in with:
- Username: `testuser`
- Password: `testpass`

If this works, the issue is with the signup write process.

---

## Common Issues & Fixes

### Issue 1: File in wrong location

**Check where your app is looking:**
```bash
cd ~/jobberman
python -c "from login_signup import get_jobbers_file; print(get_jobbers_file())"
```

**Make sure file is there:**
```bash
ls -la ~/jobberman/Jobbers.txt
```

### Issue 2: Permission denied

**Fix permissions:**
```bash
chmod 644 ~/jobberman/Jobbers.txt
chmod 644 ~/jobberman/Jobber.txt
```

### Issue 3: File not being created

**Create manually:**
```bash
cd ~/jobberman
touch Jobbers.txt
touch Jobber.txt
touch jobs.json
```

### Issue 4: Old code still running

**Clear cache and reload:**
```bash
cd ~/jobberman
find . -type d -name __pycache__ -exec rm -r {} +
```

Then reload web app in Web tab.

---

## Verify the Fix

### Test 1: Check file after signup

1. Sign up with username: `testuser2`
2. In bash console:
```bash
cat ~/jobberman/Jobbers.txt
```

You should see:
```
(username:testuser2,password:yourpassword)
```

### Test 2: Check Python can read it

```bash
cd ~/jobberman
python -c "from login_signup import jobberid; print(jobberid())"
```

Should show: `{'testuser2': 'yourpassword'}`

---

## Still Not Working?

### Enable Debug Mode Temporarily

1. Edit your WSGI file in PythonAnywhere
2. Add at the top:

```python
import sys
import logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
```

3. Reload web app
4. Try signing up
5. Check error log in Web tab

### Check Error Log

In Web tab, click on **"Error log"** link. Look for:
- File permission errors
- Path errors
- Import errors

---

## Quick Test Commands

Run these in PythonAnywhere bash:

```bash
cd ~/jobberman

# Check files exist
ls -la *.txt

# Check Python can import
python -c "from login_signup import jobberid; print('Import OK')"

# Check file path
python -c "from login_signup import get_jobbers_file; print(get_jobbers_file())"

# Check users
python -c "from login_signup import jobberid; print(jobberid())"

# Test write
echo "(username:test,password:test)" >> Jobbers.txt
cat Jobbers.txt
```

---

## After Fix: Update Workflow

When you make changes:

1. **Local:** 
   ```bash
   git add .
   git commit -m "Your changes"
   git push
   ```

2. **PythonAnywhere:**
   ```bash
   cd ~/jobberman
   git pull
   ```

3. **Web tab:** Click "Reload"

---

## Contact Info

If still having issues, check:
1. PythonAnywhere forums
2. Error log in Web tab
3. Run `debug_info.py` and share output

The updated code should fix the file path issues!

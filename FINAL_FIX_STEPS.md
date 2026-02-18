# FINAL FIX - Step by Step

## The Real Issue

The problem is likely that **environment variables aren't set** in your PythonAnywhere WSGI file. This causes session issues.

---

## Fix It Now (5 Minutes)

### Step 1: Push Latest Code

On your computer:
```bash
git add .
git commit -m "Add environment variable fallback and diagnostics"
git push
```

### Step 2: Update PythonAnywhere Code

In PythonAnywhere **Bash** console:
```bash
cd ~/jobberman
git pull
```

### Step 3: Set Environment Variables in WSGI File

1. Go to **Web** tab in PythonAnywhere
2. Find **"Code"** section
3. Click the WSGI configuration file link (e.g., `/var/www/yourname_pythonanywhere_com_wsgi.py`)
4. **DELETE EVERYTHING** in that file
5. Copy the content from `wsgi_template.py` (I created it for you)
6. **IMPORTANT:** Change `YOUR_USERNAME` to your actual PythonAnywhere username
7. Click **"Save"** (top right)

### Step 4: Reload Web App

1. Still in **Web** tab
2. Click the big green **"Reload"** button
3. Wait 10 seconds

### Step 5: Test

1. Go to your website
2. Try signing up with a **brand new username**
3. Should work now! ✅

---

## Quick Copy-Paste WSGI Content

Replace `YOUR_USERNAME` with your actual username, then paste this into your WSGI file:

```python
import sys
import os
import logging

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

# CHANGE THIS - Replace YOUR_USERNAME
project_home = '/home/YOUR_USERNAME/jobberman'

if project_home not in sys.path:
    sys.path = [project_home] + sys.path

os.chdir(project_home)

# Set environment variables
os.environ['SECRET_KEY'] = '37d17883380e7759b136d1e5ebb1d2403e538a2c5c1a11391294844a46728420'
os.environ['FLASK_ENV'] = 'production'

try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(project_home, '.env'))
except:
    pass

from app import app as application
```

---

## Verify It Works

### Run Diagnostic Script

In PythonAnywhere Bash:
```bash
cd ~/jobberman
python full_diagnostic.py
```

This will show you:
- ✅ If SECRET_KEY is set
- ✅ If files exist
- ✅ If users can be read
- ✅ If Flask app loads

### Check Error Log

In **Web** tab, click **"Error log"** to see any errors.

---

## Still Having Issues?

### Test 1: Check if environment variable is set

In Bash console:
```bash
cd ~/jobberman
python3 << 'EOF'
import os
os.environ['SECRET_KEY'] = '37d17883380e7759b136d1e5ebb1d2403e538a2c5c1a11391294844a46728420'
from app import app
print("Secret key:", app.secret_key[:30])
EOF
```

Should show your secret key.

### Test 2: Manually create a user

```bash
cd ~/jobberman
echo "(username:testuser,password:testpass)" >> Jobbers.txt
cat Jobbers.txt
```

Then try logging in with:
- Username: testuser
- Password: testpass

### Test 3: Check file permissions

```bash
cd ~/jobberman
ls -la Jobbers.txt
chmod 644 Jobbers.txt
```

---

## What Each File Does

| File | Purpose |
|------|---------|
| `wsgi_template.py` | Template for your WSGI file |
| `full_diagnostic.py` | Check everything is working |
| `PYTHONANYWHERE_ENV_SETUP.md` | Detailed environment setup guide |
| `app.py` | Now has fallback secret key |

---

## Expected Result

After following these steps:

✅ Signup creates account  
✅ Login works immediately  
✅ Sessions persist  
✅ No "Username not found" error  
✅ Can browse jobs after login  

---

## The Key Fix

The WSGI file MUST have:
```python
os.environ['SECRET_KEY'] = 'your-secret-key-here'
```

BEFORE importing your app:
```python
from app import app as application
```

This ensures Flask has the secret key when it initializes.

---

## Need More Help?

1. Run `full_diagnostic.py` and share the output
2. Check the Error log in Web tab
3. Make sure WSGI file has environment variables
4. Make sure you replaced YOUR_USERNAME in WSGI file

---

This should definitely fix it! The environment variable is the missing piece. 🔑

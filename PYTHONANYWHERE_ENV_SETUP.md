# Setting Up Environment Variables on PythonAnywhere

## Method 1: WSGI File (Recommended)

### Step 1: Open WSGI Configuration

1. Go to PythonAnywhere **Web** tab
2. Find the **"Code"** section
3. Click on the WSGI configuration file link
   - It looks like: `/var/www/yourname_pythonanywhere_com_wsgi.py`

### Step 2: Update WSGI File

Replace ALL content with this:

```python
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/YOUR_USERNAME/jobberman'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set environment variables
os.environ['SECRET_KEY'] = '37d17883380e7759b136d1e5ebb1d2403e538a2c5c1a11391294844a46728420'
os.environ['FLASK_ENV'] = 'production'

# Load .env file if it exists (optional)
try:
    from dotenv import load_dotenv
    project_folder = os.path.expanduser(project_home)
    load_dotenv(os.path.join(project_folder, '.env'))
except:
    pass

# Import your Flask app
from app import app as application
```

**IMPORTANT:** Replace `YOUR_USERNAME` with your actual PythonAnywhere username!

### Step 3: Save and Reload

1. Click **"Save"** (top right corner)
2. Go back to **Web** tab
3. Click green **"Reload"** button
4. Wait 10 seconds

---

## Method 2: .env File (Alternative)

If you prefer using .env file:

### Step 1: Create .env in PythonAnywhere

In PythonAnywhere **Bash** console:

```bash
cd ~/jobberman
nano .env
```

### Step 2: Add Content

Paste this:
```
SECRET_KEY=37d17883380e7759b136d1e5ebb1d2403e538a2c5c1a11391294844a46728420
FLASK_ENV=production
```

### Step 3: Save

Press `Ctrl+X`, then `Y`, then `Enter`

### Step 4: Verify

```bash
cat .env
```

You should see your environment variables.

---

## Method 3: Virtualenv Environment Variables

### Step 1: Find Your Virtualenv

In **Web** tab, look for **"Virtualenv"** section.

### Step 2: Edit postactivate

In Bash console:

```bash
nano ~/.virtualenvs/YOUR_VENV_NAME/bin/postactivate
```

### Step 3: Add Variables

Add these lines:
```bash
export SECRET_KEY='37d17883380e7759b136d1e5ebb1d2403e538a2c5c1a11391294844a46728420'
export FLASK_ENV='production'
```

Save and reload web app.

---

## Verify Environment Variables Work

### Test in Bash Console:

```bash
cd ~/jobberman
python3 -c "import os; from app import app; print('SECRET_KEY:', app.secret_key[:20] + '...')"
```

Should show your secret key (first 20 characters).

---

## Complete WSGI File Example

Here's the complete WSGI file you should use:

```python
import sys
import os
import logging

# Set up logging
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

# Add your project directory to the sys.path
project_home = '/home/YOUR_USERNAME/jobberman'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Change working directory
os.chdir(project_home)

# Set environment variables BEFORE importing app
os.environ['SECRET_KEY'] = '37d17883380e7759b136d1e5ebb1d2403e538a2c5c1a11391294844a46728420'
os.environ['FLASK_ENV'] = 'production'

# Try to load .env file (optional backup)
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(project_home, '.env'))
    logging.info("Loaded .env file")
except Exception as e:
    logging.info(f"Could not load .env: {e}")

# Import your Flask app
try:
    from app import app as application
    logging.info("Flask app imported successfully")
except Exception as e:
    logging.error(f"Error importing app: {e}")
    raise

# Log startup info
logging.info(f"Project home: {project_home}")
logging.info(f"Python path: {sys.path}")
logging.info(f"Working directory: {os.getcwd()}")
```

**Remember to replace YOUR_USERNAME!**

---

## After Setting Environment Variables

1. **Save** WSGI file
2. **Reload** web app
3. **Test** signup again
4. Check **Error log** if issues persist

---

## Troubleshooting

### Check if environment variables are set:

In Bash console:
```bash
cd ~/jobberman
python3 << EOF
import os
os.environ['SECRET_KEY'] = '37d17883380e7759b136d1e5ebb1d2403e538a2c5c1a11391294844a46728420'
from app import app
print("Secret key set:", app.secret_key[:20])
EOF
```

### Check Error Log:

In **Web** tab, click **"Error log"** link to see any errors.

---

## Quick Fix Checklist:

- [ ] Update WSGI file with environment variables
- [ ] Replace YOUR_USERNAME with actual username
- [ ] Save WSGI file
- [ ] Reload web app
- [ ] Test signup with NEW username
- [ ] Check error log if issues

---

The WSGI file method (Method 1) is the most reliable for PythonAnywhere!

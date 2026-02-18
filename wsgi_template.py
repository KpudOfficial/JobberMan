# COPY THIS ENTIRE FILE CONTENT TO YOUR PYTHONANYWHERE WSGI FILE
# Location: /var/www/yourname_pythonanywhere_com_wsgi.py
# 
# IMPORTANT: Replace YOUR_USERNAME with your actual PythonAnywhere username!

import sys
import os
import logging

# Set up logging to see what's happening
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

# ============================================
# CHANGE THIS LINE - Replace YOUR_USERNAME
# ============================================
project_home = '/home/YOUR_USERNAME/jobberman'
# ============================================

# Add your project directory to Python path
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Change to project directory
os.chdir(project_home)
logging.info(f"Changed directory to: {os.getcwd()}")

# ============================================
# SET ENVIRONMENT VARIABLES HERE
# ============================================
os.environ['SECRET_KEY'] = '37d17883380e7759b136d1e5ebb1d2403e538a2c5c1a11391294844a46728420'
os.environ['FLASK_ENV'] = 'production'
logging.info("Environment variables set")

# Try to load .env file as backup (optional)
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(project_home, '.env'))
    logging.info("Loaded .env file")
except Exception as e:
    logging.info(f"No .env file loaded: {e}")

# Import Flask app
try:
    from app import app as application
    logging.info("Flask app imported successfully")
    logging.info(f"Secret key configured: {application.secret_key[:20]}...")
except Exception as e:
    logging.error(f"ERROR importing Flask app: {e}")
    import traceback
    traceback.print_exc()
    raise

# Log important paths
logging.info(f"Project home: {project_home}")
logging.info(f"Python path: {sys.path[:3]}")
logging.info(f"Working directory: {os.getcwd()}")

# This is what PythonAnywhere will run
# application = your Flask app

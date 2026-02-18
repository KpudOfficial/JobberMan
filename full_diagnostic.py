"""
Complete diagnostic script for PythonAnywhere
Run this: python full_diagnostic.py
"""
import os
import sys

print("=" * 60)
print("COMPLETE DIAGNOSTIC FOR PYTHONANYWHERE")
print("=" * 60)

# 1. Python and System Info
print("\n1. SYSTEM INFORMATION")
print("-" * 60)
print(f"Python Version: {sys.version}")
print(f"Current Directory: {os.getcwd()}")
print(f"Script Location: {os.path.abspath(__file__)}")

# 2. Environment Variables
print("\n2. ENVIRONMENT VARIABLES")
print("-" * 60)
secret_key = os.environ.get('SECRET_KEY')
if secret_key:
    print(f"SECRET_KEY: {secret_key[:20]}... (found)")
else:
    print("SECRET_KEY: NOT SET")

flask_env = os.environ.get('FLASK_ENV')
print(f"FLASK_ENV: {flask_env if flask_env else 'NOT SET'}")

# 3. File Paths
print("\n3. FILE PATHS")
print("-" * 60)
try:
    from login_signup import get_jobbers_file, BASE_DIR
    print(f"BASE_DIR: {BASE_DIR}")
    jobbers_file = get_jobbers_file()
    print(f"Jobbers.txt path: {jobbers_file}")
    print(f"Jobbers.txt exists: {os.path.exists(jobbers_file)}")
    
    if os.path.exists(jobbers_file):
        size = os.path.getsize(jobbers_file)
        print(f"Jobbers.txt size: {size} bytes")
        print(f"Readable: {os.access(jobbers_file, os.R_OK)}")
        print(f"Writable: {os.access(jobbers_file, os.W_OK)}")
except Exception as e:
    print(f"ERROR: {e}")

# 4. File Contents
print("\n4. FILE CONTENTS")
print("-" * 60)
try:
    if os.path.exists(jobbers_file):
        with open(jobbers_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if content:
                print(f"Content:\n{content}")
                print(f"Number of lines: {len(content.splitlines())}")
            else:
                print("File is EMPTY")
    else:
        print("File does NOT exist")
except Exception as e:
    print(f"ERROR reading file: {e}")

# 5. User Parsing
print("\n5. USER PARSING TEST")
print("-" * 60)
try:
    from login_signup import jobberid, login
    users = jobberid()
    print(f"Number of users found: {len(users)}")
    if users:
        print("Users:")
        for username, password in users.items():
            print(f"  - {username}: {password}")
    else:
        print("NO USERS FOUND")
    
    # Test login function
    usernames, passwords = login()
    print(f"\nLogin function returned:")
    print(f"  Usernames: {usernames}")
    print(f"  Passwords: {passwords}")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()

# 6. Flask App Test
print("\n6. FLASK APP TEST")
print("-" * 60)
try:
    from app import app
    print(f"Flask app imported: SUCCESS")
    print(f"Secret key: {app.secret_key[:20]}...")
    print(f"Debug mode: {app.debug}")
except Exception as e:
    print(f"ERROR importing Flask app: {e}")
    import traceback
    traceback.print_exc()

# 7. Write Test
print("\n7. WRITE TEST")
print("-" * 60)
try:
    test_file = os.path.join(BASE_DIR, 'test_write.txt')
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("test")
    print(f"Write test: SUCCESS")
    print(f"Test file created at: {test_file}")
    os.remove(test_file)
    print(f"Test file removed: SUCCESS")
except Exception as e:
    print(f"Write test FAILED: {e}")

# 8. Recommendations
print("\n8. RECOMMENDATIONS")
print("-" * 60)

issues = []

if not secret_key:
    issues.append("❌ SECRET_KEY not set - Set in WSGI file")

if not os.path.exists(jobbers_file):
    issues.append("❌ Jobbers.txt doesn't exist - Will be created on first signup")

if os.path.exists(jobbers_file) and os.path.getsize(jobbers_file) == 0:
    issues.append("⚠️  Jobbers.txt is empty - No users registered yet")

if os.path.exists(jobbers_file) and len(users) == 0 and os.path.getsize(jobbers_file) > 0:
    issues.append("❌ File has content but no users parsed - Regex issue")

if not issues:
    print("✅ Everything looks good!")
else:
    for issue in issues:
        print(issue)

print("\n" + "=" * 60)
print("DIAGNOSTIC COMPLETE")
print("=" * 60)

# 9. Next Steps
print("\nNEXT STEPS:")
if not secret_key:
    print("1. Set SECRET_KEY in WSGI file (see PYTHONANYWHERE_ENV_SETUP.md)")
if not os.path.exists(jobbers_file):
    print("2. Try signing up - file will be created automatically")
if len(users) == 0 and os.path.exists(jobbers_file) and os.path.getsize(jobbers_file) > 0:
    print("3. Check file format - should be: (username:name,password:pass)")

print("\nFor detailed help, see: PYTHONANYWHERE_ENV_SETUP.md")

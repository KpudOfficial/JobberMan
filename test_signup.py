"""
Test script to verify signup/login works
Run this locally before deploying: python test_signup.py
"""
import os
from login_signup import jobberid, get_jobbers_file, ensure_file_exists

print("Testing Signup/Login System")
print("=" * 50)

# Test 1: Check file path
jobbers_file = get_jobbers_file()
print(f"\n1. Jobbers.txt path: {jobbers_file}")
print(f"   File exists: {os.path.exists(jobbers_file)}")

# Test 2: Ensure file exists
ensure_file_exists(jobbers_file)
print(f"\n2. After ensure_file_exists:")
print(f"   File exists: {os.path.exists(jobbers_file)}")

# Test 3: Write a test user
print(f"\n3. Writing test user...")
with open(jobbers_file, 'a', encoding='utf-8') as f:
    f.write("(username:testuser,password:testpass)\n")
print(f"   Written successfully")

# Test 4: Read users
print(f"\n4. Reading users...")
users = jobberid()
print(f"   Found {len(users)} users")
print(f"   Users: {users}")

# Test 5: Check if test user exists
if 'testuser' in users:
    print(f"\n5. ✅ Test user found!")
    print(f"   Username: testuser")
    print(f"   Password: {users['testuser']}")
else:
    print(f"\n5. ❌ Test user NOT found!")
    print(f"   This indicates a problem with the regex parsing")

print("\n" + "=" * 50)
print("Test complete!")
print("\nIf test user was found, the system should work on PythonAnywhere")
print("If not, there's an issue with the regex pattern")

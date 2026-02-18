"""
Debug script to check file paths and permissions on PythonAnywhere
Run this in PythonAnywhere bash console: python debug_info.py
"""
import os
from login_signup import jobberid, get_jobbers_file

print("=" * 50)
print("DEBUG INFORMATION")
print("=" * 50)

# Check current directory
print(f"\nCurrent Directory: {os.getcwd()}")

# Check script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Script Directory: {script_dir}")

# Check Jobbers.txt path
jobbers_file = get_jobbers_file()
print(f"\nJobbers.txt Path: {jobbers_file}")
print(f"Jobbers.txt Exists: {os.path.exists(jobbers_file)}")

if os.path.exists(jobbers_file):
    print(f"Jobbers.txt Size: {os.path.getsize(jobbers_file)} bytes")
    print(f"Jobbers.txt Readable: {os.access(jobbers_file, os.R_OK)}")
    print(f"Jobbers.txt Writable: {os.access(jobbers_file, os.W_OK)}")
    
    # Read content
    with open(jobbers_file, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"\nJobbers.txt Content:\n{content}")
        print(f"Number of lines: {len(content.splitlines())}")

# Check jobberid function
print("\n" + "=" * 50)
print("TESTING jobberid() FUNCTION")
print("=" * 50)
users = jobberid()
print(f"Number of users found: {len(users)}")
print(f"Users: {users}")

# Check Jobber.txt
jobber_file = os.path.join(script_dir, 'Jobber.txt')
print(f"\nJobber.txt Path: {jobber_file}")
print(f"Jobber.txt Exists: {os.path.exists(jobber_file)}")

# Check jobs.json
jobs_file = os.path.join(script_dir, 'jobs.json')
print(f"\njobs.json Path: {jobs_file}")
print(f"jobs.json Exists: {os.path.exists(jobs_file)}")

print("\n" + "=" * 50)
print("If you see 0 users but the file has content,")
print("there might be a regex parsing issue.")
print("=" * 50)

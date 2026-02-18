import json
import re
import os

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

usernameRegex = r'(username:)([A-Za-z]*\D[A-Za-z]*)'
username = re.compile(usernameRegex)
userpasswordRegex = r'(password:)([A-Za-z0-9?&_:"-;.\\*\+]*)'
userpassword = re.compile(userpasswordRegex)

def get_jobbers_file():
    """Get the full path to Jobbers.txt"""
    return os.path.join(BASE_DIR, 'Jobbers.txt')

def ensure_file_exists(filepath):
    """Ensure the file exists, create if it doesn't"""
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            pass
    return filepath

def jobberid():
    jobbers = dict()
    jobbers_file = get_jobbers_file()
    ensure_file_exists(jobbers_file)
    
    try:
        with open(jobbers_file, 'r', encoding='utf-8') as jbdb:
            lines = jbdb.readlines()
            for line in lines:
                if line.strip():  # Skip empty lines
                    jobbername = username.findall(line)
                    jobberpassword = userpassword.findall(line)
                    if jobbername and jobberpassword:
                        jobbers.update({jobbername[0][1]:jobberpassword[0][1][0:-1]})
    except Exception as e:
        print(f"Error reading Jobbers.txt: {e}")
    
    return jobbers

def login():
    usernames = list()
    passwords = list()
    jobbers = [jobber for jobber in jobberid().items()]
    for jobber in jobbers:
        usernames.append(jobber[0].lower().strip())
        passwords.append(jobber[1])
    return usernames, passwords

if __name__ == "__main__":
    jobber = login()
    print(jobber)
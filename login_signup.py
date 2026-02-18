import json
import re

usernameRegex = r'(username:)([A-Za-z]*\D[A-Za-z]*)'
username = re.compile(usernameRegex)
userpasswordRegex = r'(password:)([A-Za-z0-9?&_:"-;.\\*\+]*)'
userpassword = re.compile(userpasswordRegex)
def jobberid():
    jobbers = dict()
    try:
        with open('Jobbers.txt','r',encoding='utf-8') as jbdb:
            lines = jbdb.readlines()
            for line in lines:
                if line.strip():  # Skip empty lines
                    jobbername = username.findall(line)
                    jobberpassword = userpassword.findall(line)
                    if jobbername and jobberpassword:
                        jobbers.update({jobbername[0][1]:jobberpassword[0][1][0:-1]})
    except FileNotFoundError:
        # Create the file if it doesn't exist
        with open('Jobbers.txt','w',encoding='utf-8') as jbdb:
            pass
    return jobbers

def login():
    usernames= list()
    passwords= list()
    jobbers = [jobber for jobber in jobberid().items()]
    for jobber in jobbers:
        usernames.append(jobber[0].lower().strip())
        passwords.append(jobber[1])
    return usernames,passwords

if __name__ == "__main__":
    jobber = login()
    print(jobber)
from flask import Flask, render_template, url_for, request, redirect, jsonify, session, flash
from jobsdb import jobs, job_model, save_applications
import json 
import os
from login_signup import login as lg, jobberid, get_jobbers_file, ensure_file_exists

# Load environment variables from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed, will use environment variables directly

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

# Pagination settings
JOBS_PER_PAGE = 6

def get_jobber_file():
    """Get the full path to Jobber.txt"""
    return os.path.join(BASE_DIR, 'Jobber.txt')

#signup and login route
@app.route('/login/',methods=["POST","GET"])
def login():
    # If user is already logged in, redirect to index
    if 'username' in session:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('userpassword', '').strip()
        confirm_password = request.form.get('confirmpassword', '').strip()
        
        # Check if it's a signup (has confirm password field)
        if confirm_password:
            # Signup logic
            if password != confirm_password:
                return render_template("login.html", error="Passwords do not match", signup_error=True)
            
            # Check if user already exists
            existing_users = lg()[0]
            if username.lower() in existing_users:
                return render_template("login.html", error="Username already exists", signup_error=True)
            
            # Save new user to Jobbers.txt
            jobbers_file = get_jobbers_file()
            ensure_file_exists(jobbers_file)
            
            try:
                with open(jobbers_file, 'a', encoding='utf-8') as jmdb:
                    jmdb.write(f'(username:{username},password:{password})\n')
                    jmdb.flush()  # Force write to disk
                    os.fsync(jmdb.fileno())  # Ensure it's written
                
                # Verify the write was successful by reading back
                user_data = jobberid()
                if username not in user_data:
                    return render_template("login.html", error="Signup failed. Please try again.", signup_error=True)
                
                # Auto login after signup
                session['username'] = username
                session.permanent = True
                return redirect(url_for('index'))
            except Exception as e:
                return render_template("login.html", error=f"Signup error: {str(e)}", signup_error=True)
        else:
            # Login logic
            try:
                user_data = jobberid()
                
                # Check if username exists and password matches
                if username.lower() in [u.lower() for u in user_data.keys()]:
                    # Find the actual username (case-insensitive)
                    actual_username = None
                    for u in user_data.keys():
                        if u.lower() == username.lower():
                            actual_username = u
                            break
                    
                    if user_data[actual_username] == password:
                        # Also log to Jobber.txt
                        jobber_file = get_jobber_file()
                        ensure_file_exists(jobber_file)
                        with open(jobber_file, 'a', encoding='utf-8') as jmdb:
                            jmdb.write(f'(username:{actual_username},password:{password})\n')
                        
                        session['username'] = actual_username
                        session.permanent = True
                        return redirect(url_for('index'))
                    else:
                        return render_template("login.html", error="Invalid password", login_error=True)
                else:
                    return render_template("login.html", error="Username not found. Please sign up first.", login_error=True)
            except Exception as e:
                return render_template("login.html", error=f"Login failed: {str(e)}", login_error=True)
    
    return render_template("login.html")
    

#login route
#Index route
@app.route("/",methods=["GET"])
@app.route("/login/index/",methods=["GET"])
def index():
    # Check if user is logged in
    if 'username' not in session:
        return redirect(url_for("login"))
    
    # Get page number from query parameter, default to 1
    page = request.args.get('page', 1, type=int)
    
    name = session['username']
    
    # Calculate pagination
    total_jobs = len(jobs)
    total_pages = (total_jobs + JOBS_PER_PAGE - 1) // JOBS_PER_PAGE
    start_idx = (page - 1) * JOBS_PER_PAGE
    end_idx = start_idx + JOBS_PER_PAGE
    paginated_jobs = jobs[start_idx:end_idx]
    
    return render_template('index.html', 
                         name=name, 
                         jobs=paginated_jobs,
                         page=page,
                         total_pages=total_pages)


#Logout route
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

#Helper fuction
def check_job(id):
    for job in jobs:
        if job['id']==id:
            return job

#applications route
@app.route("/application/<id>")
def job_id(id):
    # Check if user is logged in
    if 'username' not in session:
        return redirect(url_for("login"))
    
    apply_job = check_job(id)
    return render_template('application.html',job=apply_job)

#application>applied route
@app.route("/application/<id>/applied",methods=["POST","GET"])
def applicant_info(id):
    # Check if user is logged in
    if 'username' not in session:
        return redirect(url_for("login"))
    
    job = check_job(id)
    applicant_info = request.form
    save_applications(applicant_info)
    return render_template('applied.html',applicant_info = applicant_info,job=job)
    


if(__name__ == "__main__"):
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
else:
    print("Invalid")
from flask import Flask, render_template, url_for, request, redirect, jsonify, session, flash
from jobsdb import jobs, job_model, save_applications
import json 
import os
from login_signup import login as lg, jobberid

# Load environment variables from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed, will use environment variables directly

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

# Pagination settings
JOBS_PER_PAGE = 6

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
            
            # Save new user
            with open('Jobbers.txt','a',encoding='utf-8') as jmdb:
                jmdb.write(f'(username:{username},password:{password})\n')
            
            # Auto login after signup
            session['username'] = username
            session.permanent = True
            return redirect(url_for('index'))
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
                        session['username'] = actual_username
                        session.permanent = True
                        return redirect(url_for('index'))
                    else:
                        return render_template("login.html", error="Invalid password", login_error=True)
                else:
                    return render_template("login.html", error="Username not found. Please sign up first.", login_error=True)
            except Exception as e:
                return render_template("login.html", error="Login failed. Please try again.", login_error=True)
    
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
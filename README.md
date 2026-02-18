# JobberMan - Job Application Platform

A Flask-based job board application where users can browse job listings and submit applications.

## Features
- User authentication (signup/login)
- Job listings with pagination
- Job application system
- Session management
- Responsive design

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Visit `http://localhost:5000`

## Deployment Options

### Option 1: Render (Recommended)

1. Create account at [render.com](https://render.com)
2. Create new Web Service
3. Connect your GitHub repository
4. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Add environment variable:
   - `SECRET_KEY`: Generate a random string
6. Deploy!

### Option 2: PythonAnywhere

1. Create account at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload files via Files tab or clone from git
3. Create new web app (Flask, Python 3.x)
4. Configure WSGI file to point to your app
5. Set environment variables in WSGI file
6. Reload web app

### Option 3: Railway

1. Create account at [railway.app](https://railway.app)
2. New Project → Deploy from GitHub
3. Add environment variables in Variables tab
4. Automatic deployment

### Option 4: Fly.io

1. Install flyctl CLI
2. Run `fly launch` in project directory
3. Follow prompts
4. Deploy with `fly deploy`

## Environment Variables

Set these in your hosting platform:

- `SECRET_KEY`: Random secret key for Flask sessions (required)
- `FLASK_ENV`: Set to `production` for deployment

## Security Notes

- Change SECRET_KEY before deployment
- User data stored in text files (consider upgrading to database for production)
- HTTPS automatically provided by hosting platforms

## File Structure

```
├── app.py                 # Main Flask application
├── jobsdb.py             # Job database and models
├── login_signup.py       # Authentication logic
├── templates/            # HTML templates
├── static/               # CSS, JS, images
├── requirements.txt      # Python dependencies
└── Procfile             # Deployment configuration
```

## Upgrading to Production

For a production-ready application, consider:

1. **Database**: Replace text files with PostgreSQL/MySQL
2. **File uploads**: Use cloud storage (AWS S3, Cloudinary)
3. **Email**: Add email verification for signups
4. **Security**: Add CSRF protection, rate limiting
5. **Monitoring**: Add error tracking (Sentry)

## License

MIT

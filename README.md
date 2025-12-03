# Postify

Postify is a Django-based web application that allows users to create, view, edit, and delete posts (tweets). It features user authentication, image uploads, and a simple, clean interface for managing personal posts.

## Features

- User registration and authentication
- Create, read, update, and delete posts (tweets)
- Image upload support for posts
- Responsive web interface
- User-specific post management

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone or download the project to your local machine.

2. Navigate to the project directory:
   ```
   cd Postify
   ```

3. Create a virtual environment (recommended):
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Apply database migrations:
   ```
   python manage.py migrate
   ```

7. Create a superuser (optional, for admin access):
   ```
   python manage.py createsuperuser
   ```

## Usage

1. Start the development server:
   ```
   python manage.py runserver
   ```

2. Open your web browser and go to `http://127.0.0.1:8000/`

3. Register a new account or log in if you already have one.

4. Start creating, viewing, editing, and deleting your posts!

## Project Structure

```
Postify/
├── db.sqlite3                    # SQLite database file
├── manage.py                     # Django management script for running commands
├── requirements.txt              # Python dependencies
├── media/                        # User-uploaded media files
│   └── photos/                   # Uploaded images for posts
├── Postify/                      # Main Django project directory
│   ├── __init__.py               # Python package initializer
│   ├── asgi.py                   # ASGI configuration for async support
│   ├── settings.py               # Django settings and configuration
│   ├── urls.py                   # Main URL configuration
│   └── wsgi.py                   # WSGI configuration for deployment
├── static/                       # Static files (CSS, JS, images)
├── tweet/                        # Main Django app for tweet functionality
│   ├── __init__.py               # Python package initializer
│   ├── admin.py                  # Django admin configuration
│   ├── apps.py                   # App configuration
│   ├── forms.py                  # Django forms for tweet creation/editing
│   ├── models.py                 # Database models (Tweet model)
│   ├── tests.py                  # Unit tests
│   ├── urls.py                   # URL patterns for tweet app
│   ├── views.py                  # View functions for handling requests
│   ├── migrations/               # Database migration files
│   │   └── 0001_initial.py       # Initial migration for Tweet model
│   └── templates/                # HTML templates
│       ├── layout.html           # Base template with navigation
│       ├── registration/         # User registration templates
│       │   ├── logged_out.html   # Logout page
│       │   ├── login.html        # Login form
│       │   └── register.html     # Registration form
│       └── tweet/                # Tweet-specific templates
│           ├── index.html        # Home page
│           ├── tweet_conform_delete.html  # Delete confirmation
│           ├── tweet_forms.html  # Create/edit tweet form
│           └── tweet_list.html   # List of all tweets
└── README.md                     # This file
```

### File Purposes

- **manage.py**: Entry point for Django management commands like running the server, creating migrations, etc.
- **requirements.txt**: Lists all Python packages required for the project.
- **db.sqlite3**: SQLite database file containing all application data.
- **Postify/settings.py**: Contains Django configuration including database settings, installed apps, middleware, and static/media file paths.
- **Postify/urls.py**: Defines URL patterns and routes requests to appropriate views.
- **tweet/models.py**: Defines the Tweet model with fields for user, text content, photo, and timestamps.
- **tweet/views.py**: Contains view functions that handle HTTP requests and return HTTP responses.
- **tweet/urls.py**: URL patterns specific to the tweet app.
- **tweet/forms.py**: Django forms for creating and editing tweets, and user registration.
- **tweet/templates/**: HTML templates for rendering the user interface.
- **media/photos/**: Directory for storing user-uploaded images.
- **static/**: Directory for static files like CSS, JavaScript, and images.

## Deployment

### Production Considerations

Before deploying to production:

1. Set `DEBUG = False` in `Postify/settings.py`
2. Configure `ALLOWED_HOSTS` with your domain name
3. Set a secure `SECRET_KEY`
4. Use a production-ready database (PostgreSQL recommended)
5. Configure static file serving
6. Set up proper logging
7. Use environment variables for sensitive settings

### Example Production Deployment (using Gunicorn and Nginx)

1. Install Gunicorn:
   ```
   pip install gunicorn
   ```

2. Run with Gunicorn:
   ```
   gunicorn Postify.wsgi:application --bind 0.0.0.0:8000
   ```

3. Configure Nginx as a reverse proxy (example config):
   ```
   server {
       listen 80;
       server_name yourdomain.com;

       location = /favicon.ico { access_log off; log_not_found off; }

       location /static/ {
           alias /path/to/your/static/files/;
       }

       location /media/ {
           alias /path/to/your/media/files/;
       }

       location / {
           include proxy_params;
           proxy_pass http://127.0.0.1:8000;
       }
   }
   ```

4. Collect static files:
   ```
   python manage.py collectstatic
   ```

5. Set up a process manager like systemd or supervisor to keep Gunicorn running.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

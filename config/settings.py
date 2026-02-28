import os
from pathlib import Path
import dj_database_url

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------
# SECURITY
# -------------------

# Get your secret key from environment variable
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "_TSFXXSHWC9pjQazXaA2Doxouzp8LdJV7ABDQJSIXijNKqX4-D5lBS-Xq-3nBuTIKY8")

# Debug mode off in production
DEBUG = os.environ.get("DEBUG", "False") == "True"

# Allowed hosts (your Render URL)
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "support-ticket-backend-ryl4.onrender.com").split(",")

# -------------------
# DATABASE
# -------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "support_ticket_db_iowd"),
        "USER": os.environ.get("DB_USER", "support_ticket_db_iowd_user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "qyjcVUc447crZoN8XLZ4A95RLBJItH0Y"),
        "HOST": os.environ.get("DB_HOST", "dpg-d6hbiivgi27c73fnjb8g-a.singapore-postgres.render.com"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

# -------------------
# STATIC FILES
# -------------------

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Use WhiteNoise to serve static files in production
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ... your other middleware
]

# -------------------
# OTHER SETTINGS
# -------------------

# Rest Framework example
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

CORS_ALLOWED_ORIGINS = [
    "https://support-ticket-backend-ryl4.onrender.com",
]
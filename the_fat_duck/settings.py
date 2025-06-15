import os
from pathlib import Path

# Project base directory (two levels up from this settings file)
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: turn off debug mode in production!
DEBUG = False

# Only these hosts/domains can serve the app
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'the-fat-duck.onrender.com']

# Secret key loaded from environment for security
SECRET_KEY = os.environ['SECRET_KEY']

# Application definitions
INSTALLED_APPS = [
    'django.contrib.admin',         # Admin site
    'django.contrib.auth',          # Authentication framework
    'django.contrib.contenttypes',  # Content type system
    'django.contrib.sessions',      # Session framework
    'django.contrib.messages',      # Messaging framework
    'django.contrib.staticfiles',   # Static file handling
    'booking',                      # Custom booking app
]

# Middleware stack
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',            # Security headers
    'whitenoise.middleware.WhiteNoiseMiddleware',               # Serve static files
    'django.contrib.sessions.middleware.SessionMiddleware',     # Session management
    'django.middleware.common.CommonMiddleware',                # Common HTTP features
    'django.middleware.csrf.CsrfViewMiddleware',                # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Associate users with requests
    'django.contrib.messages.middleware.MessageMiddleware',     # Cookie- and session-based messaging
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # Clickjacking protection
]

# Root URL configuration module
ROOT_URLCONF = 'the_fat_duck.urls'

# Template engine configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],               # Additional template directories
        'APP_DIRS': True,         # Look for templates in app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',   # Add request to context
                'django.contrib.auth.context_processors.auth',  # Add user to context
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application entry point
WSGI_APPLICATION = 'the_fat_duck.wsgi.application'

# Database configuration (SQLite for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Use WhiteNoise to serve static files efficiently in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

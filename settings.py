from pathlib import Path

# Base directory of the project (where manage.py is)
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'j((b&u5!=s2fn7be+7^4lf8f+qzoh4362+bquihy^vwg7e5ivs'

DEBUG = True  # Set to False in production!

ALLOWED_HOSTS = []  # Add your domains or IPs here in production

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sign',  # Your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'worm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Your global templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Important for auth and more
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'worm.wsgi.application'

# Database: SQLite for dev, change in production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),  # Convert Path to string to fix TypeError
    }
}

# Password validation (default recommended validators)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # your static files folder

# Media files (uploaded files)
MEDIA_URL = '/media/'  # URL prefix for media files
MEDIA_ROOT = BASE_DIR / 'media'  # Folder on disk where media files are stored

# Custom user model
AUTH_USER_MODEL = 'sign.CustomUser'

# Authentication redirects
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'

# Session and CSRF cookie security (good for development)
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Avoid warnings about default primary key field type (Django 3.2+)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# GENRAL PATHS:
# Enviroment variables are key important to keep the project secure and flexible.
# The most sensible key are saved in .env file outside the Djang's directory, but they are loaded here when Django needs them
# Tthe other Djangos's variables are set here. 
# Therefore, this sctructure need two paths: one for the Django's project (BASE_DIR) and another for the project at all (BASE_DIR_UMBRELLA).
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# __file__ works only when settings.py file is called from the shell!
# it means, the variable BASE_DIR will be not set by runing the code here, but by running the code in the shell!
# for test only, use the python terminal to set the path manually, e.g.: 
# __file__ = 'musicplayer\django01\django01\settings.py'

BASE_DIR = Path(__file__).resolve().parent.parent # check the number of '.parent'! It is 2x because BASE_DIR is the Django's project directory and settings.py has 2 levels above: backend/backend/settings.py. 

BASE_DIR_UMBRELLA = BASE_DIR.parent # here is the project directory at all, where all others files and directory outside de Django´s project are, e.g. Vue.js, git, .env etc.

# **** SECURITY WARNING ****
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

load_dotenv(dotenv_path=os.path.join(BASE_DIR_UMBRELLA,'.env')) # .env on .gitignore and .dockerignore!

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')         # secrte and strong key! 
DEBUG = os.getenv('DEBUG', 'False') == 'True'       # don't run with debug turned on in production!
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# SECURITY 'security.W...' (https://docs.djangoproject.com/en/5.1/ref/settings/#security)
# OBSERVATION:
# Django's server does not support HTTPS and make difficult to test the security settings locally (e.g. localhost:8000)
# By the other hand, ajust all variables according to test locally and production is not a good practice.
# on solution is to controle the security settings using the env variable (DEBUG), set at the .env file; i.e. only on place!
# Securitty Middleware [see MIDDLEWARE below] 
# HTTP Strict Transport Security:
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0   # SecurityMiddleware will set this header on all HTTPS responses if non-zero integer value here (e.g. 31536000) [60*60*24*365 # 31536000 = 1 year in seconds]                                      
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG  # SecurityMiddleware will add the includeSubDomains directive to the Strict-Transport-Security header if True [= assuming all subdomains are served exclusively using HTTPS], otherwise the site may still be vulnerable via an insecure connection to a subdomain.
SECURE_HSTS_PRELOAD = not DEBUG             # SecurityMiddleware will add the preload directive to the Strict-Transport-Security header if True [= the site is included in the HSTS preload list], which is a list of sites that are hardcoded into browsers as HTTPS only.
# SSL Redirect:
SECURE_SSL_REDIRECT = not DEBUG             # SecurityMiddleware will permanently redirect all HTTP connections to HTTPS. # https://docs.djangoproject.com/en/5.1/ref/middleware/#ssl-redirect
# Cross Site Request Forgery Protection: 
SESSION_COOKIE_SECURE = not DEBUG           # SecurityMiddleware will set the session cookie with the Secure flag. With this flag set, the browser will prevent the cookie from being sent over an unencrypted HTTP connection.
CSRF_COOKIE_SECURE = not DEBUG              # SecurityMiddleware will set the CSRF cookie with the Secure flag. With this flag set, the browser will prevent the cookie from being sent over an unencrypted HTTP connection.

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

################################################
# App music_player_app definition:

INSTALLED_APPS = [
    "django.contrib.admin", # Django's admin site (https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#module-django.contrib.admin). For admin user: python manage.py createsuperuser
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "music_player_app",
    "api",
    "rest_framework"
]

# USER & LOGIN/LOGOUT:
AUTH_USER_MODEL = 'music_player_app.CustomUser' # This tells Django that the user model to use throughout the project is the CustomUser class implemented  in music_player_app/models.py

# URLS for login and logout... rooting
LOGIN_URL = '/login/'           # url for login
LOGIN_REDIRECT_URL = '/home/'   # redirection after login
LOGOUT_REDIRECT_URL = '/login/' # or '/'       # redirection after logout. '/' is the home page (root). see urls.py
ROOT_URLCONF = 'backend.urls'   # ESSENTIAL!!! the root URL configuration for the Djang's project. It is the first file that Django will look for when the project is started
WSGI_APPLICATION = 'backend.wsgi.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MIDDLEWAR ~ SecurityMiddleware (SEE ABOVE)
# https://docs.djangoproject.com/en/5.1/ref/middleware/#module-django.middleware.security
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # templates folder, where the html files are stored!
        'APP_DIRS': True, # True to look for html on subfolders of templates
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]




# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# here ajusted to use PostgreSQL instead of Djang's default SQLite
# also set for different scenarios, development (DEBUG=False) and production (DEBUG=False)
# for example, when DEBUG=True, the database is set to SQLite, which is a simple and easy to use database, perfect for development, and has no problem of connections and functions such manage.py mingrate.

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'HOST': os.getenv('POSTGRES_HOST', 'db'),
            'PORT': os.getenv('POSTGRES_PORT', '5432'),
        }
    }



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Media files (images, videos, etc)
# where media files are stored and how they are accessed.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Django REST Framework settings: # authentication and permissions for the API.
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
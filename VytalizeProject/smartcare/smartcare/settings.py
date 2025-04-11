from pathlib import Path
import os

# --- BASE DIRECTORY ---
BASE_DIR = Path(__file__).resolve().parent.parent


# --- SECURITY SETTINGS ---
SECRET_KEY = 'django-insecure-REPLACE_ME_FOR_PRODUCTION'
DEBUG = True  # ❗ Set to False in production
ALLOWED_HOSTS = []  # Add domain/IP in production


# --- INSTALLED APPS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local Apps
    'accounts',

    # Third-Party
    'qr_code',  # For QR code integration
]


# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# --- ROOT CONFIG ---
ROOT_URLCONF = 'smartcare.urls'


# --- TEMPLATES ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
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


# --- WSGI / ASGI ---
WSGI_APPLICATION = 'smartcare.wsgi.application'
ASGI_APPLICATION = 'smartcare.asgi.application'


# --- DATABASE ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --- AUTH PASSWORD VALIDATION ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- LANGUAGE & TIME ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# --- STATIC & MEDIA FILES ---
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# --- DEFAULT FIELD TYPE ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- EMAIL CONFIGURATION ---
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Use SMTP in prod
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'


# --- QR CODE SETTINGS ---
QR_CODE_CACHE_ALIAS = 'default'  # Optional customization


# --- LOGIN REDIRECTS ---
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard_doctor'  # or dashboard_patient depending on role
LOGOUT_REDIRECT_URL = 'home'


# --- FILE UPLOAD MAX SIZE (OPTIONAL) ---
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10 MB

# Email settings for notifications
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'SmartCare <your_email@gmail.com>'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'jobs',
    'users',
    'api',
]

MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware', ...]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticatedOrReadOnly'],
}

CORS_ALLOWED_ORIGINS = ['http://localhost:3000']
DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql', 'NAME': 'jobboard_db', ...}}

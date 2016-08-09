from .base import *

DEBUG = False

# Security-related settings
ALLOWED_HOSTS = ["*"]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

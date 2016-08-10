from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['127.0.0.1']

DEBUG = True

SECRET_KEY = 'iq+w=cd9b76pf72=+#o0&sr8k#l#dx_8(f8!my^rq*)5fstl$c'

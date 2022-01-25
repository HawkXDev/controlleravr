from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '$%^&1278fdshfsjkcxre-$)@--fhajsdhfkvhcxzuklbfe32614igdsakg$euh*$x#g216lskv'

STATIC_ROOT = BASE_DIR / 'static'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '164.92.218.30', 'controlleravr.ru']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CSRF_TRUSTED_ORIGINS = ['https://controlleravr.ru']

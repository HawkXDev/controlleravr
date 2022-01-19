from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '$%^&1278fdshfsjkcxre-$)@--fhajsdhfkvhcxzuklbfe32614igdsakg$euh*$x#g216lskv'

STATIC_ROOT = BASE_DIR / 'static'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

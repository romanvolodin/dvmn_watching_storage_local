import os
from environs import Env


env = Env()
env.read_env()

db_engine = env.str("DB_ENGINE")
db_host = env.str("DB_HOST")
db_port = env.int("DB_PORT")
db_name = env.str("DB_NAME")
db_user = env.str("DB_USER")
db_password = env.str("DB_PASSWORD")

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'HOST': db_host,
        'PORT': db_port,
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG", False)

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

# coding=utf-8

import os

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd9qsbdsjaghrtd',
        'USER': 'ewqryngxsqzazf',
        'PASSWORD': '09bbc7c19fea7db6e197aeb6fde78a29eede870c01595198ba33d373c83361cd',
        'HOST': 'ec2-35-153-91-18.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
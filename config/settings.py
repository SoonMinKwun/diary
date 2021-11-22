"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
#----------------------[KEY 보안용]----------------------#
import os, json
from django.core.exceptions import ImproperlyConfigured
#--------------------------------------------------------#

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

#----------------------------[KEY 보안용]----------------------------#
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        print("check: ", secrets[setting])
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)
#--------------------------------------------------------------------#

SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'diary.apps.DiaryConfig',
    'common.apps.CommonConfig',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # 템플릿 위치 설정
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# MongoDB 사용, 이름은 diary

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'diary',
    }
}
# DATABASES = {
#         'default': {
#             'ENGINE': 'djongo',
#             'NAME': 'DIARY',
#             'HOST': 'mongodb+srv://DiaryAdmin:diary159357456@cluster0.znsdz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',
#             'USER': 'DiaryAdmin',
#             'PASSWORD': 'diary159357456',
#         }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 로그인 성공시 메인으로 리다이렉트
LOGIN_REDIRECT_URL = '/'
# 로그아웃 성공시 메인으로 리다이렉트
LOGOUT_REDIRECT_URL = '/'

#-------------------------------[AWS]-------------------------------#
# S3 세팅
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' # 기본 파일 저장 경로 S3로 설정
AWS_STORAGE_BUCKET_NAME = 'mydiaryimg' # S3 버킷 이름

# AWS 세팅
AWS_ACCESS_KEY_ID = get_secret("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_secret("AWS_SECRET_ACCESS_KEY")
AWS_REGION = 'ap-northeast-2'
AWS_QUERYSTRING_AUTH = False
#-------------------------------------------------------------------#

#-----------------------------[Global]------------------------------#
imgread = None # write에 이미지 파일명을 넣어주기 위한 전역변수
#-------------------------------------------------------------------#
# 파라미터 개수 기본 1000이므로 늘려놓음
DATA_UPLOAD_MAX_NUMBER_FIELDS = 4000
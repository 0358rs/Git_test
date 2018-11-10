import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'EB', # DB名を設定
        'USER': 'root', # DBへ接続するユーザIDを設定
        'PASSWORD': '80249satoshi', # DBへ接続するユーザIDのパスワードを設定
        'HOST': '',
        'PORT': '3306',
    }
}

DEBUG = True
import os


class Development:
    SECRET_KEY = 'dev'
    DEBUG = True


class Production:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False

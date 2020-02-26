import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '4cyjhdf-fusdf84i-usao9di'
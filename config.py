import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "YOUR SECRET KEY HERE!"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
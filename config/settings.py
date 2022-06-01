import os

from flask import current_app 
class Config:
    DEFAULT = False
    PORT = os.environ.get('PORT') or 5000
    ENV = os.environ.get('FLASK_ENV')
    FLASK_APP = os.environ.get('APP_NAME')
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
   

    
    

class production(Config):
    DEBUG = False
    PORT = os.environ.get('PORT') or 8080

class testing(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    


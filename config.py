import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'this-is-a-secret-key'
    UPLOADED_PHOTOS_DEST = os.getcwd() + '/uploads'
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@host/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

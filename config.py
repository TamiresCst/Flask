import os
class Config(object):
    SECRET_KEY = os.urandom(32)
    basedir = os.path.abspath(os.path.dirname(__file__))

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Config.basedir, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    IP_HOST = 'localhost'
    PORT_HOST = 3000
import os

BASEDIR = os.path.dirname(os.path.realpath(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SERVER_NAME = 'localhost:3321'


class Development(Config):
    DEBUG = True
    DEVELOPMENT = True
    ENV = 'development'


class Production(Config):
    DEVELOPMENT = False
    DEBUG = False
    ENV = 'production'


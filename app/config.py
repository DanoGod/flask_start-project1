import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
  #SQLALCHEMY_DATABASE_URI = os.environ.get(DATABASE_URL= 'postgresql://tzsshfpwcedadb:3ec3a8fc7d850a27e7a9b0d30eb5670242bfe29310e4e3ec11fb9b653c796419@ec2-54-211-176-156.compute-1.amazonaws.com:5432/df8re81nhb40o'
#HEROKU_POSTGRESQL_WHITE_URL='postgres://hdnlabkxftjbps:e26cf85f5c3325b20cdef268969129ea4c951992525c7c7841090f3ab7386d09@ec2-54-211-176-156.compute-1.amazonaws.com:5432/d7dq8vt06titvf') 
    #SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
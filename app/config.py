import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
  SQLALCHEMY_DATABASE_URI = os.environ.get(DATABASE_URL='postgresql://ogwukdxbbvzqpn:7d4ea6caa5329fe6172fa78529a5ed70f68c0494094f81412d345d22fc73405a@ec2-3-211-37-117.compute-1.amazonaws.com:5432/d2h4p8c0jlk4p2'
HEROKU_POSTGRESQL_BRONZE_URL='postgresql://axxyovrmzgxbqp:c2da95f64c20bf1034eecbeab94d8f0c5766d640f6df08ae94cb324df7edce37@ec2-18-233-83-165.compute-1.amazonaws.com:5432/dedh35u6bg884o') 
    #SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
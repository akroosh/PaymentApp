class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ="postgresql+psycopg2://akroosh:admin@localhost/payment"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
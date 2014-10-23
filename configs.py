import os

class Config():
    JSON_AS_ASCII = False
    SECRET_KEY = "SUPER SECRET KEY THAT NO ONE CAN FIND"


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///td.db"
    DEBUG = True
    TESTING = False
    SECRET_KEY = "SUPER SECRET KEY THAT NO ONE CAN FIND"
    JSONIFY_PRETTYPRINT_REGULAR = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://td:LNWRcTyWEb9XF2cS@129.242.219.41/td"
    DEBUG = False
    TESTING = False
    SERVER_NAME = "dataforeninga.org"
    SECRET_KEY = os.urandom(24)
    JSONIFY_PRETTYPRINT_REGULAR = False
    CSRF_ENABLED = True

    USER_ENABLE_EMAIL = True
    USER_ENABLE_USERNAME = False
    USER_ENABLE_REGISTRATION = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///tests/test.db"
    DEBUG = False
    TESTING = True


class TravisTestingConfig(TestConfig):
    TESTING = False
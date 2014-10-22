class Config():
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://td:LNWRcTyWEb9XF2cS@129.242.219.41/td"
    JSON_AS_ASCII = False
    SECRET_KEY = "SUPER SECRET KEY THAT NO ONE CAN FIND"


class DevConfig(Config):
    DEBUG = True
    TESTING = False
    SECRET_KEY = "SUPER SECRET KEY THAT NO ONE CAN FIND"
    JSONIFY_PRETTYPRINT_REGULAR = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SERVER_NAME = "dataforeninga.org"
    SECRET_KEY = '\xf0\xd0\xe9`\xa9\xdc\xe3\x7fQ\xe2\x8d\xeb\xd7\xc4\xb2C\xa8\xb0\xa0\x91\xb9\xff\x03\x8c'
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
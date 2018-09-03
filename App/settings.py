def get_database_uri(dbinfo):
    host = dbinfo.get('HOST') or 'localhost'
    port = dbinfo.get('PORT') or '3306'
    user = dbinfo.get('USER') or 'root'
    password = dbinfo.get('PASSWORD') or '123456'
    db = dbinfo.get('DB') or 'mydb'
    driver = dbinfo.get('DRIVER') or 'pymysql'
    type = dbinfo.get('TYPE') or 'mysql'
    encoding = dbinfo.get('ENCODING') or 'utf8'
    return '{}+{}://{}:{}@{}:{}/{}?charset={}'.format(type, driver, user, password, host, port, db, encoding)


class Config:
    DEBUG = True
    TESTTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class TestConfig(Config):
    DEBUG = False

    DATABASE = {
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123456',
        'DB': 'mydb',
        'DRIVER': 'pymysql',
        'TYPE': 'mysql',
        'ENCODING': 'utf8',
    }


class DevelopConfig(Config):
    TESTTING = False

    DATABASE = {
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123456',
        'DB': 'mydb',
        'DRIVER': 'pymysql',
        'TYPE': 'mysql',
        'ENCODING': 'utf8',
    }

    SQLALCHEMY_DATABASE_UII = get_database_uri(DATABASE)


class ProductConfig(Config):
    DEBUG = False
    TESTTING = False

    DATABASE = {
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123456',
        'DB': 'mydb',
        'DRIVER': 'pymysql',
        'TYPE': 'mysql',
        'ENCODING': 'utf8',
    }


config = {
    'develop': DevelopConfig,
    'test': TestConfig,
    'product': ProductConfig,
    'default': DevelopConfig,
}
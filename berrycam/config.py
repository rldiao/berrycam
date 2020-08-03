class BaseConfig:
    SECRET_KEY = 'GDtfDCFYjD'


class ProdConfig(BaseConfig):
    DEBUG = False
    TESTING = False


class DevConfig(BaseConfig):
    DEBUG = False
    TESTING = True

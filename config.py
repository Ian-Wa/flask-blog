
import os


class Config:

    SECRET_KEY = 'PxsNJYQD_hKc0EehtCarvw'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringascool:access@localhost/blogs'

    # email configutions
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS =True
    MAIL_USERNAME='ian.wanjira@student.moringaschool.com'
    MAIL_PASSWORD='sct221-0494'

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass

    pass



class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
     if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringascool:access@localhost/blogs'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringascool:access@localhost/blogs'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test':TestConfig,
}

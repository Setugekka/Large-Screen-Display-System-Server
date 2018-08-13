#encoding:utf-8
#程序配置文件
class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:0000@116.196.90.212/LSDS'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY = ''

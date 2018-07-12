# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_admin import Admin
from flask_babelex import Babel



db = SQLAlchemy()
admins = Admin(name='后台管理系统',template_mode='bootstrap3')
babel = Babel()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    admins.init_app(app)
    babel.init_app(app)
    db.init_app(app)


    #注册蓝图函数
    from .main import main_Blueprint as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

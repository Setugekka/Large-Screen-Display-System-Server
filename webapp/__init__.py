# coding=utf-8
from flask import Flask, redirect, url_for, render_template
from flask_principal import identity_loaded, UserNeed, RoleNeed
from config import DevConfig
from extensions import login_manager, principals
from flask_login import current_user
from models import *
from RestfulApi.city import city_blueprint
from RestfulApi.generator import generator_blueprint
from RestfulApi.repaircar import repaircar_blueprint
from RestfulApi.vehicles import vehicles_blueprint
from flask_cors import CORS

def create_app(object_name):
    app = Flask(__name__)
    CORS(app) #解决调试过程中，跨域请求问题
    app.config.from_object(DevConfig)
    db.init_app(app)
    login_manager.init_app(app)
    principals.init_app(app)
    # db.init_app(app)
    #模块注册
    app.register_blueprint(city_blueprint)
    app.register_blueprint(generator_blueprint)
    app.register_blueprint(repaircar_blueprint)
    app.register_blueprint(vehicles_blueprint)
    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        identity.user = current_user
        if hasattr(current_user, "username"):
            identity.provides.add(UserNeed(current_user.username))
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))
    return app

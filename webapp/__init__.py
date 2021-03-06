# coding=utf-8
from flask import Flask, redirect, url_for, render_template
from flask_principal import identity_loaded, UserNeed, RoleNeed
from config import DevConfig
from extensions import login_manager, principals
from flask_login import current_user
from models import *
from socket import socketio
from flask_cors import CORS
from RestfulApi.dev import dev_blueprint
from RestfulApi.p_expert import p_expert_blueprint
from RestfulApi.p_repair import p_repair_blueprint
from RestfulApi.p_manager import p_manager_blueprint
from RestfulApi.p import p_blueprint
from RestfulApi.m_equipment import m_equipment_blueprint
from RestfulApi.m_stuff import m_stuff_blueprint
from RestfulApi.m_material import m_material_blueprint
from RestfulApi.generator import generator_blueprint
from RestfulApi.repaircar import repaircar_blueprint
from RestfulApi.vehicles import vehicles_blueprint
from RestfulApi.urgent_material import urgentmaterial_bluprint
from RestfulApi.organization import organization_blueprint
from RestfulApi.institutions import institutions_blueprint
from RestfulApi.plan import plan_blueprint
from RestfulApi.training import training_blueprint
from RestfulApi.report import report_blueprint
from RestfulApi.city_list import city_blueprint
from RestfulApi.c_manager import c_manager_blueprint
from RestfulApi.v_manager import v_manager_blueprint
from RestfulApi.weather_data import weather_data_blueprint
from Controller import form_entry_system


def create_app(object_name):
    app = Flask(__name__)
    CORS(app) #解决跨域请求问题 也可调用response() 都可以
    app.config.from_object(DevConfig)
    db.init_app(app)
    login_manager.init_app(app)
    principals.init_app(app)
    socketio.init_app(app)
    #模块注册
    # 调试模块
    app.register_blueprint(dev_blueprint)
    #大屏api模块
    app.register_blueprint(p_expert_blueprint)
    app.register_blueprint(p_manager_blueprint)
    app.register_blueprint(p_repair_blueprint)
    app.register_blueprint(p_blueprint)
    app.register_blueprint(m_equipment_blueprint)
    app.register_blueprint(m_stuff_blueprint)
    app.register_blueprint(m_material_blueprint)
    app.register_blueprint(generator_blueprint)
    app.register_blueprint(repaircar_blueprint)
    app.register_blueprint(vehicles_blueprint)
    app.register_blueprint(urgentmaterial_bluprint)
    app.register_blueprint(organization_blueprint)
    app.register_blueprint(institutions_blueprint)
    app.register_blueprint(plan_blueprint)
    app.register_blueprint(training_blueprint)
    app.register_blueprint(report_blueprint)
    app.register_blueprint(city_blueprint)
    app.register_blueprint(c_manager_blueprint)
    app.register_blueprint(v_manager_blueprint)
    app.register_blueprint(weather_data_blueprint)

    #表单录入系统
    app.register_blueprint(form_entry_system)
    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        identity.user = current_user
        if hasattr(current_user, "username"):
            identity.provides.add(UserNeed(current_user.username))
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))
    return app

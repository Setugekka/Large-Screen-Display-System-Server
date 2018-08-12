from flask import Blueprint, jsonify,request
from . import response
from webapp.models import p_expert,p_manager,p_repair
p_blueprint = Blueprint(
    'p',
    __name__,
    url_prefix="/p"
)
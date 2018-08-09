from flask import Blueprint, redirect, render_template, url_for
city_blueprint = Blueprint(
    'city',
    __name__,
    url_prefix="/city"
)
@city_blueprint.route('/',methods=('GET', 'POST'))
def hello():
    return "hello world"
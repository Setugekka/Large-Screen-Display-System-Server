#encoding:utf-8
from . import form_entry_system
from flask import render_template
@form_entry_system.route('index')
def index():
    return render_template('system/index.html')

@form_entry_system.route('index2')
def index2():
    return render_template('system/index2.html')
from flask import Blueprint
form_entry_system = Blueprint(
    'form_entry_system',
    __name__,
    url_prefix="/form_entry_system/"
)
import view
import api
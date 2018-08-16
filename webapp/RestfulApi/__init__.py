from flask import make_response
def response(context):
    r = make_response(context)
    r.headers['Access-Control-Allow-Origin'] = '*'
    r.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    r.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return r

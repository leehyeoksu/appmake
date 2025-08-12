from flask import Blueprint

app=Blueprint('v1', __name__,url_prefix='/v1')


@app.route('/users')
def usets():
    return "v1"
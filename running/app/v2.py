from flask import Blueprint

app=Blueprint('v2', __name__,url_prefix='/v2')


@app.route('/users')
def usets():
    return "v2"
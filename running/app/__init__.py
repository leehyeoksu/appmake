

from flask import Flask,request,render_template,redirect,url_for,abort
from flask.views import View, MethodView
app = Flask(__name__,static_folder='static', template_folder='templates')

class MYView(MethodView):
    def get(self,user_id):
        if user_id is None:
            #reutrn a list of users
            return "all"
        else:
            #expose a single user
            return "one"
        
    def post(self):

        return "post"
    def put(self,user_id):
        return "put"
    def delete(self,user_id):
        return "delete"
myview=MYView.as_view("users")
app.add_url_rule('/users/', defaults={'user_id': None}, view_func=myview, methods=['GET'])
app.add_url_rule('/users/', view_func=myview, methods=['POST'])
app.add_url_rule('/users/<int:user_id>', view_func=myview, methods=['GET', 'PUT', 'DELETE'])   

class UserView(View):
    def dispatch_request(self):
        users = [
            {"id": 1, "name": "혁수", "email": "hyeoksu@example.com"},
            {"id": 2, "name": "철수", "email": "chulsoo@example.com"},
            {"id": 3, "name": "영희", "email": "younghee@example.com"}
        ]
        return render_template('test.html', users=users)
app.add_url_rule('/users', view_func=UserView.as_view('user_view'))


@app.route("/log")
def test_log():
    app.logger.info("This is an info message")
    app.logger.warning("This is a warning message") 
    
    return redirect(url_for("user_view"))

@app.errorhandler(403)
def permission_denied(error):
    return "403", error.code
@app.route("/")
def index():
    return redirect(url_for('uer_list'))
@app.route('/users')
def uer_list():
    abort(403)



@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



'''@app.route('/users/<username>')
def get_user(username):
    return username'''

@app.route('/posts/<int:post_id>')
def get_post(post_id):
    return f"Post ID: {post_id}"

@app.route('/uuids/<uuid:uuid_value>')
def get_uuid(uuid_value):
    return f"UUID: {uuid_value}"    





def do_the_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "admin" and password == "1234":
        return "로그인 성공!"
    else:
        return "로그인 실패!"

def show_the_login_form():
    return render_template('login.html')


@app.route('/login',methods=['GET', 'POST'] )
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()



@app.route('/index')
@app.route("/")
def hello_world():
    return "hello first flask coding"


from flask import Flask,request,render_template

app = Flask(__name__,static_folder='static', template_folder='templates')



#@app.route('/login',methods=['GET', 'POST'] )
#def login():
   # if request.method == 'POST':
        #return do_the_login()
    #else:
       # return show_the_login_form()
@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/users/<username>')
def get_user(username):
    return username

@app.route('/posts/<int:post_id>')
def get_post(post_id):
    return f"Post ID: {post_id}"

@app.route('/uuids/<uuid:uuid_value>')
def get_uuid(uuid_value):
    return f"UUID: {uuid_value}"    

@app.route('/index')
@app.route("/")
def hello_world():
    return "hello first flask coding"




if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development mode
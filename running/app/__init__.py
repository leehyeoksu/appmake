

from flask import Flask,request,render_template,redirect,url_for,abort
from flask.views import View, MethodView

from .v1 import app as v1_app
from .v2 import app as v2_app
app = Flask(__name__,static_folder='static', template_folder='templates')

app.register_blueprint(v1_app)
app.register_blueprint(v2_app) 



# ====== MethodView: /api/users ======
class MYView(MethodView):
    def get(self, user_id=None):
        if user_id is None:
            return "all"
        return "one"

    def post(self):
        return "post"

    def put(self, user_id):
        return "put"

    def delete(self, user_id):
        return "delete"

myview = MYView.as_view("api_users")  # 엔드포인트 이름: api_users
# 리스트
app.add_url_rule("/api/users/", defaults={"user_id": None}, view_func=myview, methods=["GET"])
# 생성
app.add_url_rule("/api/users/", view_func=myview, methods=["POST"])
# 단건 조회/수정/삭제
app.add_url_rule("/api/users/<int:user_id>", view_func=myview, methods=["GET", "PUT", "DELETE"])

# ====== View: /users (템플릿 렌더) ======
class UserView(View):
    def dispatch_request(self):
        users = [
            {"id": 1, "name": "혁수", "email": "hyeoksu@example.com"},
            {"id": 2, "name": "철수", "email": "chulsoo@example.com"},
            {"id": 3, "name": "영희", "email": "younghee@example.com"},
        ]
        return render_template("test.html", users=users)

# 엔드포인트 이름을 명시하면 오타 방지됨
app.add_url_rule("/users", view_func=UserView.as_view("user_view"))

# ====== 로그 테스트 → user_view로 이동 ======
@app.route("/log")
def test_log():
    app.logger.info("This is an info message")
    app.logger.warning("This is a warning message")
    return redirect(url_for("user_view"))

# ====== 403 예외/핸들러 ======
@app.errorhandler(403)
def permission_denied(error):
    return "403", error.code

@app.route("/forbidden")
def forbidden():
    abort(403)

# ====== 루트는 user_view로 리다이렉트 ======
@app.route("/")
def index():
    return redirect(url_for("user_view"))

# ====== 기타 예제 ======
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)

@app.route("/posts/<int:post_id>")
def get_post(post_id):
    return f"Post ID: {post_id}"

@app.route("/uuids/<uuid:uuid_value>")
def get_uuid(uuid_value):
    return f"UUID: {uuid_value}"
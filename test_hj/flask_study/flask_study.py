import json

from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route("/aaa",methods=['POST','GET'])
def hello():
    return "Hello World!"

@app.route("/bbb",methods=['POST','GET'])
def hellobbb():
    json1 = {'error': 'Unauthorizedckkkkkkk111'}
    resp = Response(json.dumps(json1), status=200,
                    mimetype='application/json')
    resp.headers["Content-Language"] = "header11111"
    return resp;

# {
#     "key1" : 1,
#     "key2" : "string",
#     "title":"9999"
# }

@app.route("/post",methods=['POST'])
def hello1():
    if request.form:
        print(request.form)
        return "request.form"
    elif 'title' in request.json:
        task = {
            'id': 1,
            'title': request.json['title'],
            'description': request.json.get('description', ""),
            'done': False
        }
        return jsonify(task), 201
    elif request.json:
        print(request.json)
        print(request.charset)
        return "request.json"
# 可以用 jsonify 返回 json 数据 jsonify( json )
# 使用 jsonify 时，返回的 http response 的 Content-Type 是 Content-Type: application/json
# 而使用json.dumps时，Content-Type则是  Content-Type: text/html; charset=utf-8
# 既然返回的是 json 数据，那么自然要指明 Content-Type 是 application/json ， 这样做是符合 HTTP 协议的规定的
# 使用 jsonify 除了让返回的 `http response符合 HTTP 协议，同时也对数据做了压缩处理，让数据体积更小。


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if 1:
            print(request.form['username'])
            print(request.form['password'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
# /user/username&908098
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/cookie')
def index():
    username = request.cookies.get('username')

@app.route("/login", methods=['POST'])
def login():
	 data = request.form.get('data')
	 data = json.loads(data)
	 username = data['username']
	 password = data['password']

@app.route("/flask/login1", methods=['POST'])
def login1():
 data = request.get_data()
 data = json.loads(data)
 username = data['username']
 password = data['password']

@app.route("/flask/login2", methods=['POST'])
def login2():
 data = request.get_json()
 username = data['username']
 password = data['password']



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6666)
    # host="0.0.0.0" 可以让服务器被公开访问 否则 只有你自己的电脑可以使用服务
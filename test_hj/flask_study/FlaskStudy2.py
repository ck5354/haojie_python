# -*- coding: utf-8 -*-

import json
import time
# from flask_cors import CORS
from flask import Response
import xml.etree.ElementTree as ET
from flask import Flask, jsonify, abort, request, make_response, url_for, redirect
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")
auth = HTTPBasicAuth()
# CORS(app)


ClientClosed = 499
J_MSG = {ClientClosed: 'ClientClosed'}


@auth.get_password
@auth.get_password
def get_password(username):
    if username == 'jiashuo':
        return "test"
    return None


@app.route('/chenkuo-aaa/post', methods=['POST'])
# @auth.login_required
def create_task():
    task = dict()
    if request.form:
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
        return "request.json"



# 可以用 jsonify 返回 json 数据 jsonify( json )
# 使用 jsonify 时，返回的 http response 的 Content-Type 是 Content-Type: application/json
# 而使用json.dumps时，Content-Type则是  Content-Type: text/html; charset=utf-8
# 既然返回的是 json 数据，那么自然要指明 Content-Type 是 application/json ， 这样做是符合 HTTP 协议的规定的
# 使用 jsonify 除了让返回的 `http response符合 HTTP 协议，同时也对数据做了压缩处理，让数据体积更小。


# @app.errorhandler 重新定义错误返回 POST http://127.0.0.1:6666/chenkuo/error  接口返回 {"error":"Unauthorizedckkkkkkk"} ，
@app.errorhandler(400)
def unauthorized(error):
    return make_response(jsonify({'error': 'Unauthorizedckkkkkkk'}), 400)


@app.route('/chenkuo/error', methods=['POST'])
def get_status():
    abort(400)


# 增加不存在的status_code进行响应。
class CustomFlaskErr(Exception):
    status_code = 400

    def __init__(self, return_code=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.return_code = return_code
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['error'] = J_MSG[self.return_code]
        return rv


@app.errorhandler(CustomFlaskErr)
def handle_flask_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/chenkuo/myerror', methods=['GET'])
# @auth.login_required
def get_error():
    raise CustomFlaskErr(ClientClosed, status_code=499)


@app.route('/chenkuo/myresponse', methods=['GET', 'POST', 'HEAD', 'DELETE', 'PUT', 'PATCH'])
def get_myresponse():
    json1 = {'error': 'Unauthorizedckkkkkkk111'}
    resp = Response(json.dumps(json1), status=200,
                    mimetype='application/json')
    resp.headers["Content-Language"] = "header11111"
    return resp;


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=6666)
    # host="0.0.0.0" 可以让服务器被公开访问 否则 只有你自己的电脑可以使用服务

import json

from flask import Flask, request, jsonify, Response

app = Flask(__name__)
# 处理JSON格式的请求数据

# 知识点1------->处理JSON格式的请求数据
# 如果POST的数据是JSON格式，request.json会自动将json数据转换成Python类型（字典或者列表）。
@app.route('/add', methods=['POST'])
def add():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    result = request.json['a'] + request.json['b']
    return str(result)

# json_data = {'a': 1, 'b': 2}
# r = requests.post("http://127.0.0.1:5000/add", json=json_data)
# print(r.text)


# 知识点2------->响应JSON-方案1
# 如果POST的数据是JSON格式，request.json会自动将json数据转换成Python类型（字典或者列表）。
@app.route('/add', methods=['POST'])
def add():
    result = {'sum': request.json['a'] + request.json['b']}
    return Response(json.dumps(result),  mimetype='application/json')

# json_data = {'a': 1, 'b': 2}
# r = requests.post("http://127.0.0.1:5000/add", json=json_data)
# print(r.text)
# 知识点3---------->如果需要服务器的HTTP响应头具有更好的可定制性
@app.route('/add', methods=['POST'])
def add():
    result = {'sum': request.json['a'] + request.json['b']}
    resp = Response(json.dumps(result),  mimetype='application/json')
    resp.headers.add('Server', 'python flask')
    return resp


# 知识点4---------->jsonify
@app.route('/add', methods=['POST'])
def add2():
    result = {'sum': request.json['a'] + request.json['b']}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888)
    # host="0.0.0.0" 可以让服务器被公开访问 否则 只有你自己的电脑可以使用服务
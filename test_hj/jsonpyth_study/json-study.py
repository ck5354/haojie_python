import jsonpath

a = {
    "resultcode": "200",
    "reason": "成功的返回",
    "result": {
        "company": "顺丰",
        "com": "sf",
        "no": "575677355677",
        "list": [
            {
                "datetime": "2013-06-25 10:44:05",
                "remark": "已收件",
                "zone": "台州市"
            },
            {
                "datetime": "2013-06-25 11:05:21",
                "remark": "快件在 台州 ,准备送往下一站 台州集散中心 ",
                "zone": "台州市"
            }
        ],
        "status": 1
    },
    "error_code": 6
}

def get_json_path(json_string,json_key):
    '''
     通过jsonpath取出json中对应的值
    :param json_string: json
    :param json_key: jsonpath eg：$.stu_info.[0].name
    :return: jsonpath匹配到的值
    '''
    return jsonpath.jsonpath(json_string,json_key)
# $.result.list[0].remark == 已收件
# $.result.list[0].remark > 0
# $.result.list[0].remark < 0
# 已收件
def assert_json_value(json_string,json_value):
    '''
    通过jsonpath断言对应值的内容
    :param json_string: json语句
    :param json_value: json判断条件 eg：$.result.list[0].remark == 已收件
    :return: 判断结果boolean类型
    '''
    if json_value.startswith("$."):
        if "==" in json_value:
            json_key = json_value.split('==')[0].replace(" ", "")
            value = json_value.split('==')[1].replace(" ", "")
            return get_json_path(json_string, json_key)[0] == value
        if ">" in json_value:
            json_key = json_value.split('>')[0].replace(" ", "")
            value = json_value.split('>')[1].replace(" ", "")
            return get_json_path(json_string, json_key)[0] > value
        if "<" in json_value:
            json_key = json_value.split('<')[0].replace(" ", "")
            value = json_value.split('<')[1].replace(" ", "")
            return int(get_json_path(json_string, json_key)[0]) < int(value)
    # else: return json_value in str(json_string)
    else:  return str(json_string).__contains__(json_value)


key_value = '已收件'
assert_json = assert_json_value(a,key_value)
print(assert_json)




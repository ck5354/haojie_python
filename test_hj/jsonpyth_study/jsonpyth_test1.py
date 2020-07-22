import jsonpath
import string


d = {
    "error_code": 0,
    "stu_info": [
        {
            "id": 2059,
            "name": "小白",
            "sex": "男",
            "age": 28,
            "addr": "河南省济源市北海大道32号",
            "grade": "天蝎座",
            "phone": "18378309272",
            "gold": 10896,
            "info": {
                "card": 434345432,
                "bank_name": '中国银行'
            }

        },
        {
            "id": 2067,
            "name": "小黑",
            "sex": "男",
            "age": 28,
            "addr": "河南省济源市北海大道32号",
            "grade": "天蝎座",
            "phone": "12345678915",
            "gold": 100
        }
    ]
}

# res = d["stu_info"][0]['name']  # 取某个学生姓名的原始方法:通过查找字典中的key以及list方法中的下标索引
# print(res)  # 输出结果是：小黑

import jsonpath

# res1 = jsonpath.jsonpath(d, '$..name')  # 嵌套n层也能取到所有学生姓名信息,$表示最外层的{}，..表示模糊匹配
# res1 = jsonpath.jsonpath(d, '$.stu_info.[0].name')  # 嵌套n层也能取到所有学生姓名信息,$表示最外层的{}，..表示模糊匹配
# print(res1)  # 输出结果是list：['小白', '小黑']

# res2 = jsonpath.jsonpath(d, '$..bank_name')
# print(res2)  # 输出结果是list：['中国银行']

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
    "error_code": 0
}
def get_json_vlue(json_string,json_path):
    return jsonpath.jsonpath(json_string,json_path)
result = get_json_vlue(a,'$.result.list[0].remark')
print(result)
print(result == ['已收件'])
def assert_json_vlue(json_sring,assert_vlue):
    json_path = assert_vlue.split('==')[0]
    vlue = assert_vlue.split('==')[1]
    return get_json_vlue(json_sring,json_path)[0] == vlue
print(assert_json_vlue(a,'$.result.list[0].remark==已收件'))


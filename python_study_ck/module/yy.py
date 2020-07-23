import requests
import random
#   ----------------------------新建配置---------------------------------
def  创建配置1():
 url ='https://jdsf-console.jdcloud.com/openApi/jdsf/createAppConfig?regionId=cn-east-2'
 a=random.choice('abcdefghijklmnopqrstuvwxyz&#%^*f')
 print(a)
 param ='{"params":{"regionId":"cn-east-2","appConfigContent":"config222","appConfigId":"","appConfigName":"config222%a","appConfigRemark":"","appConfigVersion":"1.1.1","appConfigVersionId":"","appName":"config222","createTime":"","parentVersionId":"","Accept-Language":"cn"}}'%(a)
 headers = {}
 headers['Cookie'] ='_ga=GA1.2.419864993.1560997787; 3AB9D23F7A4B3C9B=VIODP3QJ2JFS75G4TRHWBLUIYZUXNLUKY5LMOJNQ5WBZLK2DIP4EIITOUBKH4WVES5VCYSIICPSNPMBR6K36CXSWQM; __jda=250736605.15609312567152073675150.1560931257.1563416620.1563523251.25; __jdv=233866958|direct|-|none|-|1564544255214; _gid=GA1.2.319845158.1565415306; pin=jdcloud-api-test; unick=jdcloud-api-test; csrfToken=3fHFTbJ_FI4ZUWk_phTRM2YJ; jdcloud_sitelang=cn; __jdc=250736605; thor=520D78BDB6E3106915005393D9283339AB820C281E44189BBA969B0B11966F4D318E8BBB89553BC8C9A8AA58E9035172379CE662D8E6A559CC60BBE58409CE967BB3C0C1841CD97E56CC001D2406386170844C8388FB41DCC8E23AA784CC6074BFA6F6E880CE21BCA7FCE0E287E3CA53DFA74A5F061295B36718E96956364C8A076E46961748A7059BFDCC420EF8A0D7D2F01E55FB25E458702FE3D73C244D04; currPage=configListManage; __jda=250736605.15609312567152073675150.1560931257.1563416620.1563523251.25; __jdb=250736605.5.15609312567152073675150|25.1563523251'
 headers['Content-Type'] = 'application/json;charset=UTF-8'
 r = requests.post(url,headers=headers,data=param)
 print(r.text)
# result = "requestId" in r.text
# assert result == True



# ------------------------------删除配置-----------------------------------------------id
def delect():
 url ='https://jdsf-console.jdcloud.com/openApi/jdsf/deleteAppConfig?regionId=cn-east-2'
 id='ac-3dpflgtkh3i8'
 param ='{"params":{"appConfigId":"%s","regionId":"cn-east-2","Accept-Language":"cn"}}'%(id)
 headers = {}
 headers['Cookie'] = '_ga=GA1.2.419864993.1560997787; 3AB9D23F7A4B3C9B=VIODP3QJ2JFS75G4TRHWBLUIYZUXNLUKY5LMOJNQ5WBZLK2DIP4EIITOUBKH4WVES5VCYSIICPSNPMBR6K36CXSWQM; __jda=250736605.15609312567152073675150.1560931257.1563416620.1563523251.25; __jdv=233866958|direct|-|none|-|1564544255214; _gid=GA1.2.319845158.1565415306; pin=jdcloud-api-test; unick=jdcloud-api-test; csrfToken=3fHFTbJ_FI4ZUWk_phTRM2YJ; jdcloud_sitelang=cn; __jdc=250736605; thor=520D78BDB6E3106915005393D9283339AB820C281E44189BBA969B0B11966F4D318E8BBB89553BC8C9A8AA58E9035172379CE662D8E6A559CC60BBE58409CE967BB3C0C1841CD97E56CC001D2406386170844C8388FB41DCC8E23AA784CC6074BFA6F6E880CE21BCA7FCE0E287E3CA53DFA74A5F061295B36718E96956364C8A076E46961748A7059BFDCC420EF8A0D7D2F01E55FB25E458702FE3D73C244D04; __jda=250736605.15609312567152073675150.1560931257.1563416620.1563523251.25; currPage=configListManage; __jdb=250736605.6.15609312567152073675150|25.1563523251'
 headers['Content-Type'] = 'application/json;charset=UTF-8'
 r = requests.post(url,headers=headers,data=param)
 print(r.text)
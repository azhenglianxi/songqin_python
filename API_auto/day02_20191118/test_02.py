#作业  构建 HTTP的请求

import  requests
#  练习requests库发送GET方式请求
#
# 【案例1】：百度首页【不带请求参数的】
# baidu = requests.get("https://www.baidu.com/")
# print(baidu.text)
# print(baidu.raw)
# print(baidu.headers)


# 【案例2】：教管系统-列出课程【带请求参数的】

# p2 =requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20')
# print('p2',p2.text)


# （2）练习requests库发送POST方式请求
#
# 【案例3】：教管系统-新增课程【data参数】
# adds ={
#      "action":"add_course",
#      "data":"""{
#      "name":"博士化学",
#      "desc":"初我 晚22上中化学课程",
#      "display_idx":"4"
# }"""
# }
# poe =requests.post("http://localhost/api/mgr/sq_mgr/",data=adds)
# print(poe.text)
# 【案例4】：教管系统-新增课程2【json参数+headers参数】
sda ="""
{
    "action":"add_course_json",
    "data":
    {
      "name":"22初中化学",
      "desc":"1初1中3212化学课程",
      "display_idx":"4"
    }
}"""
# header={"Content-Type":"application/json"}
# ef =requests.post("http://localhost/apijson/mgr/sq_mgr/",data=sda.encode(),headers=header)
# print(ef.text)

# #.（3）练习requests库发送带cookies的请求
cookies={'cookies_are':'wh6txtypan4ubx0buexb0wl6f8hmhoxv'}
sdd =requests.post('http://localhost/api/mgr/loginReq',data=cookies)
print(sdd.text)


# # 【案例5】：用户登录【cookies】
# land ={"username":"auto","password":"sdfsdfsdf"}
# loc=requests.post('http://localhost/api/mgr/loginReq',data=land)
# print(loc.text)
# print(loc.cookies)
# print(loc.headers['Set-Cookie'])

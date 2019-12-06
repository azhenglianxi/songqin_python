import requests
# 练习 get 请求不带参数
# 1-1  requests库提供了get方法，传一个url路径作为参数
# 1-2  返回的是一个response 对象（包括响应头、响应状态码、响应消息体等内容）
# r = requests.get('https://www.baidu.com/')
# 1-3  文本格式的响应消息体内容，输出
# print(r.text)



# p2 =requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20')
# print('p2',p2.text)






#  请求带参数 get
# paylod={
#     'action':'list_course',
#     'pagenum':11,
#     'pagesize':200
# }
#
# r = requests.get('http://localhost/api/mgr/sq_mgr/',params=paylod)
# print(r.text)

# 案例3 ：post请求 (练习data 参数)
# 3-1 定义一个字典 叫payload
payload={
    'action':'add_course',
    'data':'''{
      "name":"初中2化学4aaa1",
      "desc":"初中224化学课程",
      "display_idx":"4"
    }
    '''
}
r=requests.post('http://localhost/api/mgr/sq_mgr/',data=payload)
print(r.text)



#案例4 新增课程2 （练习json  参数+headers 参数）
#4-1 定义一个字符串 交 payload 内容是要转的 请求体消息
payload="""
        {
         "action":"add_course_json",
         "data":{
         "name":"初中2化学"，
         "desc":"chuzhonghauxue 1",
         "display_idx":"4"
         }
       }
"""
# 4-2 定义一个字典名字 heafer 内容是1个名称为content-type的 请求头
#header={'Content-Type':'application/json'}
# 4-3 调用requests的post的方法，根据帮助文档，data参数如果是 字符串 则 按原格式发出去
# 4-4 字符串中如果包含中文，则需要encode 转码
# 4-5 根据帮助文档 headers 参数传递的是字典格式
#po=requests.post('http://localhost/apijson/mgr/sq_mgr/',data=payload.encode(),headers=header)

#print(po.text)


# 案例5 用户登录接口 练习cookie
# payload2 ={"username":"auto","password":"sdfsdfsdf"}
# ro =requests.post("http://localhost/api/mgr/loginReq",data=payload2)
# print(ro)


# 5-1 输出整个响应头 能输出
# print(ro.headers)
# 5-2 输出响应头中 set-Cookie 的内容
# print(ro.headers['set-Cookie'])


# *************四种获取【响应中】-消息体的内容的方法 ####
# 第一种方法 ：叫文本响应的内容，通常需要获取页面HTML内容时用
# print(ro.text)
# 第二种方法叫响应的内容，通常是在爬虫下载网页图片或文件时用
# print(ro.content)
# #  第三种方法 ：叫做原始格式响应内容。很少用
# print(ro.raw)

# 第四种方法： 叫做json解码响应内容 返回的是字典格式 非常实用
# 但是需要明确接口返回的内容是json格式，否则 会被抛出异常
# print(ro.json())
# print(ro.raise_for_status())




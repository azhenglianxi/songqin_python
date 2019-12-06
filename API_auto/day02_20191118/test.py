import requests
import pprint  #pprint 库是格式化输出，对输出信息进行排版的
import json

#案例1：练习get请求 不带参数

#1-1  requests库提供了get方法，传一个url路径作为参数
#1-2  返回的是一个response 对象（包括响应头、响应状态码、响应消息体等内容）
r=requests.get('http://www.baidu.com')
#1-3  文本格式的响应消息体内容，输出
print(r.text)


#案例2：练习get请求，带请求参数
#2-1 把请求参数放置url中，也是可以的，类似为【案例1】
r=requests.get('http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20')
#2-2  文本格式的响应消息体内容，输出
print(r.text)

########换一种方式实现【案例2】##########
#2-3 定义一个字典，名字叫payload
payload={
    'action':'list_course',
    'pagenum':1,
    'pagesize':20
}
#2-4 通过params参数，把get的请求参数以字典的格式传递
#2-5 根据帮助文档，params参数会把字典格式转换为表单格式放在url的后面
r=requests.get('http://localhost/api/mgr/sq_mgr/',params=payload)
#2-6  文本格式的响应消息体内容，输出
print(r.text)



#案例3：post请求（练习data参数）
#3-1 定义一个字典，叫payload
payload={
    'action':'add_course',
    'data':'''{
      "name":"初中化学aaa1",
      "desc":"初中化学课程",
      "display_idx":"4"
    }
    '''
}
#3-2 调用requests的post函数，第一个参数是url，再把字典格式的数据，传递给data
#3-3 根据帮助文档，如果传的是字典格，会字典编码为表单
r=requests.post('http://localhost/api/mgr/sq_mgr/',data=payload)
#3-4  文本格式的响应消息体内容，输出
print(r.text)


#案例四：新增课程2（练习json参数+headers参数）
#4-1 定义一个字符串，叫payload，内容是要转递的请求体消息
payload='''
        {
          "action" : "add_course_json",
          "data"	 : {
            "name":"小学数学",
            "desc":"sss",
            "display_idx":"4"
          }
        }
        '''
#4-2 定义一个字典，名字叫header，内容是1个名称为Content-Type的请求头
header={'Content-Type':'application/json'}
#4-3 调用requests的post方法，根据帮助文档，data参数如果传递的是字符串，则按原格式直接发出去。
#4-4 字符串中包含有中文，需要通过encode转码
#4-5 根据帮助文档，headers参数传递的是字典格式。
r=requests.post('http://localhost/apijson/mgr/sq_mgr/',data=payload.encode(),headers=header)
# print(r.text)

################案例五的第二种方法############
#4-20 定义一个字典，叫payload，内容是要转递的请求体消息
payload={
          'action' : 'add_course_json',
          'data'	 : {
            'name':'小学数www学qqqq',
            'desc':'sss',
            'display_idx':'4'
          }
        }
#4-21 把payload字典转换为json字符串,变量名称叫：jsonStr
jsonStr=json.dumps(payload)
#4-22 输出该字符串，可以看到，它的确把单引号，变为了双引号。表明它的确被转换成了json格式。
print(jsonStr)
#4-23 用str函数，查看它的类型为str类型
print(str(jsonStr))
#4-24 得出结论，dict 经过json.dumps 转换后，可以得到string格式的json内容

#4-25 定义一个字典，名字叫header，内容是1个名称为Content-Type的请求头
header={'Content-Type':'application/x-www-form-urlencoded'}

#4-26 还是像第一种方式一样，如果data传递的是一个字符串，那么按原格式直接发布出去
r=requests.post('http://localhost/apijson/mgr/sq_mgr/',data=jsonStr,headers=header)
#上面的语句，等同于下面的
#r=requests.post('http://localhost/apijson/mgr/sq_mgr/',data=json.dumps(payload),headers=header)
print(r.text)


############案例五的第三种方法############
#4-30 定义一个字典，叫payload，内容是要转递的请求体消息
payload={
          'action' : 'add_course_json',
          'data'	 : {
            'name':'小学数www学qqqq',
            'desc':'sss',
            'display_idx':'4'
          }
        }
header={'Content-Type':'application/x-www-form-urlencoded'}
#4-31 根据帮助文档，json 参数如果传递的是字典格式，则会编码为json字符串，相当于data=json.dumps(payload)
r=requests.post('http://localhost/apijson/mgr/sq_mgr/',json=payload,headers=header)
print(r.text)

#案例5 用户登录接口，练习cookies
payload={"username":"auto","password":"sdfsdfsdf"}
r=requests.post('http://localhost/api/mgr/loginReq',data=payload)
print(r.text)
#5-1 输出整个响应头的内容，能输出
print(r.headers)
#5-2 输出响应头种，Set-Cookie的内容
print(r.headers['Set-Cookie'])


#######################四种获取【响应中】-【消息体的内容】的方法############################
#第一种方法：叫文本响应内容，通常需要获取网页html内容时用
print(r.text)
#第二种方法：叫字节响应内容，通常是在爬虫下载网页图片或文件时用
print(r.content)
#第三种方法：叫原始格式响应内容，很少用
print(r.raw)
#第四种方法：叫JSON解码响应内容，返回的是字典格式，非常实用
#但是需要明确接口返回的内容是json格式，否则会抛异常
print(r.json())









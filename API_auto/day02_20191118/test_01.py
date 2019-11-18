import requests
#不带参数
# r = requests.get('https://www.baidu.com/')
# print(r.text)


# 请求带参数 get
# paylod={
#     'action':'list_course',
#     'pagenum':11,
#     'pagesize':200
# }
#
# r = requests.get('http://localhost/api/mgr/sq_mgr/',params=paylod)
# print(r.text)

#案例3 ：post请求
payload={
    'action':'add_course',
    'data':'''{
      "name":"初中化学aaa1",
      "desc":"初中化学课程",
      "display_idx":"4"
    }
    '''
}

r=requests.post('http://localhost/api/mgr/sq_mgr/',data=payload)
print(r.text)

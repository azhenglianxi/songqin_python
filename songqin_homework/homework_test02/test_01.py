filedir='0005_1.txt'

def putInfoToDict(fileName):
    resDict ={}
    with open(filedir) as fo:
        lines =fo.read().splitlines()
        for one in lines:
            one =one.replace('\t','').replace("'",'').replace('(','').replace(")",'').replace(';',',')
            temp =one.split(',')
            lessonid =temp[2].strip()
            checkintime =temp[0].strip()
            useid =temp[1].strip()
            #格式化 规范输入
            #infoDict ={useid:{lessonid:checkintime}}
            infoDict ={'lessonid':lessonid,'checkintime':checkintime}
            if useid not in resDict:
                resDict[useid]=[infoDict ]
            else:
                resDict[useid].append(infoDict )
        return resDict
import pprint
res =putInfoToDict(filedir)

pprint.pprint(res)


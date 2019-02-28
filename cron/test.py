# -*- coding: UTF-8 -*-

'''
1、读取指定目录下的所有文件
2、读取指定文件，输出文件内容
3、创建一个文件并保存到指定目录
'''
import os
from bs4 import BeautifulSoup
import re
import uuid
import json
dict = {}
# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        print (child)  # .decode('gbk')是解决中文显示乱码问题
        readFile(child)


# 读取文件内容并打印
def readFile(filename):
    # fopen = open(filename, 'r')  # r 代表read
    # for eachLine in fopen:
    #     print( "读取到得内容如下：", eachLine)
    # fopen.close()
    soup = BeautifulSoup(open(filename))
    sel=soup.select('div > select')
    if len(sel)>0:
        print(sel)
        for a in sel:
            op = a.select('option')
            print(a.id,op)
            list=[]
            for b in op:
                print(b.text)
                dic={}
                dic['value']=b.text
                dic['label'] = b.text
                list.append(dic)
                # print(uuid.uuid1())
            dict['未指定'+str(uuid.uuid1())]=list
  # '性别': [{ value: '1', label: '男' }, { value: '2', label: '女' }],


if __name__ == '__main__':
    filePath = "D:\\FileDemo\\Java\\myJava.txt"
    filePathI = "D:\\FileDemo\\Python\\pt.py"
    filePathC = "/home/dhlsoft/下载/司库html"
    eachFile(filePathC)
    # print(dict)
    j = json.dumps(dict,ensure_ascii=False)
    print(j)
    # readFile(filePath)
    # writeFile(filePathI)
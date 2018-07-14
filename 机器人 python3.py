# coding=utf-8

import urllib
import urllib.request
import urllib.parse
import json


def getResponse(url):
    page = urllib.request.urlopen(url)     #获取的url包
    response = page.read()         #读取包的文件
    return response

if __name__ == '__main__':
    key = '60e15fe9b5594287b5da1a5c0a81dbc5'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='

    name = input('请输入你的名字: ')  #录入用户名
    while True:
        info = input(name + '：')      #读取输入信息
        request = api + urllib.parse.quote(info)     #请求信息构建
        response = getResponse(request)    #获取响应信息
        print('request: ' + request)       #打印request信息
        print('response: ' + request)      #打印response信息
        dic_json = json.loads(response)    #将已编码的 JSON 字符串解码为 Python 对象
        print('图灵机器人: ' + dic_json['text'])   #将dic_json格式转换

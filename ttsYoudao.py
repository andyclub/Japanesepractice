# 直接在有道API的示例文档上修改的，通过参数q传递阅读内容，生成日语合成语音，返回文件路径。
# 原示例代码：
# https://ai.youdao.com/console/#/service-singleton/speech-synthesis/see-demo?productId=5&id=640
# API文档：
# https://ai.youdao.com/DOCSIRMA/html/%E8%AF%AD%E9%9F%B3%E5%90%88%E6%88%90TTS/API%E6%96%87%E6%A1%A3/%E8%AF%AD%E9%9F%B3%E5%90%88%E6%88%90%E6%9C%8D%E5%8A%A1/%E8%AF%AD%E9%9F%B3%E5%90%88%E6%88%90%E6%9C%8D%E5%8A%A1-API%E6%96%87%E6%A1%A3.html
import sys
import uuid
import requests
import hashlib
import time
from configparser import ConfigParser
import os

# 从同一目录下的youdao.ini读取有道api需要的APP_Key, APP_SECRET
YOUDAO_URL = 'https://openapi.youdao.com/ttsapi'
conn = ConfigParser()
file_path = os.path.join(os.path.abspath('.'),'youdao.ini')
if not os.path.exists(file_path):
    raise FileNotFoundError("文件不存在")
conn.read(file_path)
APP_KEY = conn.get('api','APP_KEY')
APP_SECRET = conn.get('api','APP_SECRET')

def encrypt(signStr):
    hash_algorithm = hashlib.md5()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()

def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)

def connect(q):
    data = {}
    data['langType'] = 'ja'
    salt = str(uuid.uuid1())
    signStr = APP_KEY + q + salt + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign
    response = do_request(data)
    contentType = response.headers['Content-Type']
    if contentType == "audio/mp3":
        millis = int(round(time.time() * 1000))
        filePath = "voiceTmp/" + str(millis) + ".mp3"
        fo = open(filePath, 'wb')
        fo.write(response.content)
        fo.close()
        return filePath
    else:
        print(response.content)


if __name__ == '__main__':
    connect("はわいい")
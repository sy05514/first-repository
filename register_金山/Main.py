import hashlib
from _md5 import md5
from urllib import request,parse
import re

baseUrl = 'https://i.wan.liebao.cn/register?'

s = hashlib.md5('aaa123456'.encode(encoding='UTF-8')).hexdigest()

print(s)

data = {
    'passport': 'luoyantes9',
    'password': '88316675d7882e3fdbe066000273842c',
    'truename': '地方',
    'service': 'https://i.wan.liebao.cn/login?go=https%253A%252F%252Fwan.liebao.cn%252F&supplier_id=2',
    'idcard': '123'
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

http_handler = request.HTTPHandler

openner = request.build_opener(http_handler)

dataEncode = parse.urlencode(data)

res = request.Request(url=baseUrl, data=bytes(dataEncode, encoding='utf-8'), headers=header)

response = openner.open(res).read().decode('utf-8')

print(response)
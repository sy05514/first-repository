from urllib import request,parse
import json

class shotMessage:


    # 跨域用车接口
    def kuayu(tel, headers):
        baseUrl = 'https://dev.kckjgs.com/register/ticket/sms?'
        data = parse.urlencode({
                'Mobile': tel
            })
        reBaseUrl = request.Request(url=baseUrl, data=bytes(data, encoding='utf-8'), headers=headers)
        try:
            res = request.urlopen(reBaseUrl).read().decode('utf-8')
            print('跨域用车接口信息为' + res)
        except:
            print('跨域用车接口调用失败')
        else:
            print('跨域用车接口调用成功')

    # 海鳗接口
    def haiman(tel, headers):
        baseUrl = 'https://haiman.io/api/phone-code/' + tel + '?'
        # 海鳗关于csum参数加密字段
        n = 5381
        for x in range(0, len(tel)):
            n += n << 5
            n += ord(tel[x])
            n &= 2147483647
        csum = hex(n).split('0x')[1]
        data = parse.urlencode({
                'csum': csum
            })
        baseUrl = baseUrl + data
        reBaseUrl = request.Request(url=baseUrl, headers=headers)
        try:
            res = request.urlopen(reBaseUrl).read().decode('utf-8')
            print('海鳗接口信息为' + res)
        except:
            print('海鳗接口调用失败')
        else:
            print('海鳗接口调用成功')

    # 柳州行政审批局
    def lzXingzheng(tel, headers):
        baseUrl = 'https://e.liuzhou.gov.cn/visit/uaRegistData/uaUserPhoneCheck'
        data = parse.urlencode({
                'uaUser.phone': tel
            })
        reBaseUrl = request.Request(url=baseUrl, data=bytes(data, encoding='utf-8'), headers=headers)
        try:
            res = request.urlopen(reBaseUrl).read().decode('utf-8')
            print('柳州行政审批局接口信息为' + res)
        except:
            print('柳州行政审批局调用失败')
        else:
            print('柳州行政审批局调用成功')
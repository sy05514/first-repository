from services.kws import shotMessage
import time

phone = '15978042383'
headers = {
    'User-Agent': 'Mozilla/5.0(iPhone;CPUiPhoneOS11_0likeMacOSX)AppleWebKit/604.1.38(KHTML,likeGecko)Version/11.0Mobile/15A372Safari/604.1SE2.XMetaSr1.0'
}
# shotMessage.kuayu(phone, headers)
for x in range(1, 100):
    shotMessage.haiman(phone, headers)
    print('第一次延时开始')
    time.sleep(61)
# shotMessage.lzXingzheng(phone, headers)
# 使用windows时，只要使用execjs，把下面的代码放到第一行即可，放在后面就没有用
import subprocess  #执行命令的
from functools import  partial  #固定某个参数的
subprocess.Popen=partial(subprocess.Popen,encoding='utf-8')

import requests
import random
import string
import execjs


def generate_random_string(length=16):
    if length == 0:
        length = 16
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    result = ""
    for i in range(length):
        result += random.choice(chars)
    return result

url='https://www.kanzhun.com/api_to/search/salary.json'
# 这是你要搜索的职位之类的，可以自己改
e='{"query":"python","cityCode":1,"industryCodes":"","pageNum":1,"limit":15}'
s=generate_random_string()
js = execjs.compile(open('kanzhun.js', mode='r',encoding='utf-8').read())
# 修改这里，将t转换为UTF-8编码
t = js.call('fn', e, s)

params={
    "b":t,
    "kiv":s
}
headers={
    'Referer':'https://www.kanzhun.com/search?cityCode=337&industryCodes=&pageNum=1&query=python&type=4',
    'Cookie':'__c=1699500140; wd_guid=fb9c882a-9b2a-49c2-9609-13e1357151a1; __g=-; historyState=state; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1699500142; __l=r=&l=%2Fapi_to%2Fhome%2Frec.json%3Fb%3D75Gia9WuHHoncXnv5vPFXg~~%26kiv%3DK6RiunplZtlRvjG3; __a=93901548.1699500140..1699500140.4.1.4.4; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1699545297; wbrwsid=39305054',
    'Content-Type':'application/x-www-form-urlencoded;charset=utf-8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}
resp=requests.get(url,params=params,headers=headers)
# print(resp.url)
# print(resp.text)
iv=s
# 这个是返回后的数据
data=resp.text
# 调用解密函数，获取解密后的数据
real_Data=js.call('fn2',data,iv)
print(real_Data)


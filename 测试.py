import subprocess  #执行命令的
from functools import  partial  #固定某个参数的
subprocess.Popen=partial(subprocess.Popen,encoding='utf-8')

import requests
import random
import string
import execjs

js = execjs.compile(open('kanzhun.js', mode='r',encoding='utf-8').read())
e='{"query":"python","cityCode":1,"industryCodes":"","pageNum":1,"limit":15}'
s='QYe6UORBFni9NDM9'
t = js.call('fn', e, s)
url='https://www.kanzhun.com/api_to/search/salary.json'
params={
    "b":t,
    "kiv":s
}

print(params)
headers={
    "Content-Type":"application/x-www-form-urlencoded",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
resp=requests.get(url,params=params,headers=headers)
print(resp.text)


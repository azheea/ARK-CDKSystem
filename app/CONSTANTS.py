"""
@FILE_NAME : CONSTANTS
-*- coding : utf-8 -*-
@Author : Zhaokugua/AzheGod.
@Time : 2022/10/11 9:40
"""
import time
import requests
import random
import datetime
import hashlib
import base64
import json
# 设置服务器open-command的token
GMkey = 'Azhegod'

# 设置服务器地址，后面不带/
Server_addr = 'http://127.0.0.1'


# 邮件默认过期时间戳（默认为邮件发送时间+30天）
Mail_default_expire_time = int((datetime.datetime.now() + datetime.timedelta(days=30)).timestamp())

# 设置CDK默认过期时间（默认为90天）
CDK_expire_day = 90

# 设置网页背景图链接，默认是/static/images/bg.jpg文件
# 也可以设置一些随机图的地址 比如https://api.mtyqx.cn/tapi/random.php
# 更多随机图地址详见我博客https://blog.jixiaob.cn/?post=93
background_image = './usr/theme/images/bg.jpg'

# 设置获取在线人数的缓存时间秒数，时间过短可能导致所有页面加载缓慢和大量的服务器查询人数请求
# 默认为1分钟
online_cache_time = 60


# 设置登录认证的密码
auth_pwd = 'Azhegod'



Server_token = GMkey
def initialize():

    # 测试是否已启用插件
    req_url = f'{Server_addr}/opencommand/api'
    json_ping = {
        'action': 'ping',
    }
    try:
        requests.post(Server_addr+"/online/v1/ping", json={"value":"/v1/ping"},verify=False)
        print('\033[0;32m连接服务器成功！\033[0m')
        return True
    except:
        return False


# 获取在线人数的缓存，加速短时间内获取在线人数的速度，减少请求服务器的速度
online_cache = (datetime.datetime.now(), 0)


def get_online():
        return 114514, None

def generate_code(code_len=6):
    all_char = '0123456789qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJIKOLP'
    index = len(all_char) - 1
    code = ''
    for _ in range(code_len):
        num = random.randint(0, index)
        # print(num)
        code += all_char[num]
    return code.upper()



def exec_command(command, uid=None):
    command = command.strip()
    if command[:5].lower() == 'sleep':
        sleep_time = command.replace('sleep', '')
        if sleep_time.isdigit():
            sleep_time = int(sleep_time)
            print(f'正在执行延时命令：sleep{sleep_time}...')
            time.sleep(sleep_time)
            return {'success': True, 'data': f'延迟命令执行{sleep_time}ms'}
        else:
            return {'success': False, 'data': f'延迟命令语法错误！正确的语法示例：sleep100'}
    command = command[1:] if command.startswith('/') or command.startswith('!') else command
    headers = {'GMKey': str(Server_token)}
    params = {
        'uid': uid,
        'charId': command
    }
    yuanchengip = Server_addr+"/admin/send/character"
    response = requests.get(yuanchengip, headers=headers, params=params).json()
    return {'success': True, 'data': response}


YSGM = {
    'enable': False,
    'MUIP_HOST': 'http://127.0.0.1:54321/api',
    'MUIP_TARGET_REGION': 'dev_test'
}

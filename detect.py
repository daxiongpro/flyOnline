import os
import time
import random
from login import Login
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, default='zm.txt')
configs = parser.parse_args()

print(configs)

def ping(ping_url='8.8.8.8',my_timeout= 6):
    """
    测试能否ping通一个网址,设置最大超时为`my_timeout` 秒
    """
    import subprocess
    p = subprocess.Popen(['ping', ping_url, '-c4'])
    try:
        p.wait(my_timeout)
    except subprocess.TimeoutExpired:
        p.kill()
        print('Ping fail. Connecting ...')
        return 1

    print('Ping success! Wait ...')
    return 0

if __name__ == '__main__':
    loginer = Login('./zm.txt')
    ping_url = 'www.baidu.com'
    counts_login = 0
    counts_test = 0
    time_s = 2
    time_pre = time_s
    while(True):
        t = ping(ping_url)
        counts_login = counts_login + t
        counts_test += 1
        print('Login times:\t', counts_login)
        print('Detect times:\t', counts_test)
        if t: #ping fail
            time_s = 2
            loginer.try_all()
        else:
            time_s = time_pre
        time_gap = int(60 * random.uniform(time_s, time_s + random.uniform(0, 5)))
        time_pre = int(time_gap / 60)
        print('Time gap: ', time_pre, 'mins', time_gap%60, 's')
        time.sleep(time_gap)

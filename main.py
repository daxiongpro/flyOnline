import os
import time
import random
from login import Login
import argparse
from ping import ping

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, default='zm.txt')
configs = parser.parse_args()


def random_sleep(mean, std, SLEEP_NUM=0):
    SLEEP_NUM += 1
    time_gap = int(random.gauss(mean, std))
    print("{}th sleep:{} min {} s".format(SLEEP_NUM, time_gap / 60, time_gap % 60))
    time.sleep(time_gap)
    return SLEEP_NUM


if __name__ == '__main__':
    SLEEP_NUM = 0
    while True:
        if not ping(url='www.baidu.com', wait=1):  # ping fail
            print("网络异常，尝试登录NBU账号")
            loginer = Login(configs.file)
            loginer.try_all()
        SLEEP_NUM = random_sleep(300, 60, SLEEP_NUM)

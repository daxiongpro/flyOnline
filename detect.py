import os
import time
import random
from login import Login
import argparse
from ping import ping

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, default='zm.txt')
configs = parser.parse_args()

def random_sleep(mean, std):
    time_gap = int(random.gauss(mean, std))
    print('Time gap: ', time_gap/60, 'mins', time_gap%60, 's')
    time.sleep(time_gap)

if __name__ == '__main__':
    loginer = Login(configs.file)
    while(True):
        if not ping(ping_url = 'www.baidu.com'):# ping fail
            loginer.try_all()
        random_sleep(300,60)


# -*- coding: utf-8 -*-
import os

def ping(url="www.baidu.com"):
    """
    测试能否ping通特定网址
    args url 
    return True 通
           False 不通
    """
    result = os.system(u"ping {} -c 4".format(url))
    if result == 0:
        print("正常")
        return True
    else:
        print("网络故障")
        return False

if __name__ == "__main__":
    result = ping()
    print(result)

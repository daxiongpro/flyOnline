# -*- coding: utf-8 -*-
import os

def ping(url="www.baidu.com", default_ip=["125.39.52.26", "106.13.147.175"]):
    """
    测试能否ping通特定网址
    args 
        -url 
        -default_ip
    return True 通
           False 不通
    """
    result = os.system(u"ping {} -c 4".format(url))
    if result == 0:
        print("ping {}正常".format(url))
        return True
    else:
        #备选机制
        print("{} 不通，下面尝试备用ip".format(url))
        for ip in default_ip:
            if os.system(u"ping {} -c 4".format(ip)) == 0: 
                return True

        print("网络异常")
        return False

if __name__ == "__main__":
    result = ping()
    print(result)

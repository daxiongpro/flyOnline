import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class Account():
    def __init__(self,filename='./zm.txt'):
        self.filename = filename
        self.accounts = self.process_file(filename) 

    def process_file(self,filename):
        accounts = {}
        for line in open(filename):
            if line != '\n':
                psd,account = line.strip().split(',')
                accounts[account] = psd
        return accounts
    def items(self):
        return self.accounts.items()

    def __delitem__(self,key):
        """
        example:
            del my_account["1611082722"]
        """
        del self.accounts[key]
    def __repr__(self):
        result = ""
        for k,v in self.accounts.items():
            result += k+','+v+'\n'
        return result
    def save(self):
        with open(self.filename,'w') as f:
            f.write(self.__repr__())

class Login:
    opt = FirefoxOptions()
    opt.add_argument('--headless')
    browser = webdriver.Firefox(options=opt)
    time.sleep(2)

    def __init__(self,filename='./zm.txt'):
        self.accounts = Account(filename)

    def clean(self):
        # unused
        for account,psd in self.accounts.items():
            if not self.login(account,psd):
                print("fail")

    def try_all(self):
        for account,psd in self.accounts.items():
            if not self.login(account,psd):
                print("login error: {},{}",account, psd)
            else:
                return

        print("all account have been tested")
            
    def login(self,account,psd):
        try:
            #solve `TimeoutException: Message: Timeout loading page after 300000ms`
            self.browser.get(r"http://10.22.63.253/0.htm")
        except Exception as e:
            print(e)
            self.browser.quit()
            self.broser = webdriver.Firefox(options=self.opt)
            self.browser.get(r"http://10.22.63.253/0.htm")

        username = self.browser.find_element_by_xpath('//input[@type="text"]')
        password = self.browser.find_element_by_xpath('//input[@type="password"]')

        username.clear()
        username.send_keys(account)
        password.clear()
        password.send_keys(psd)

        commit = self.browser.find_element_by_id("submit")
        commit.click()
        time.sleep(2)
        if "Drcom" not in self.browser.title:
            commit = self.browser.find_element_by_id("submit")
            commit.click()
            time.sleep(2)
            return False
        else:
            print('Online now. Account used: ', account)
            time.sleep(2)
            return True
if __name__ == '__main__':
    loginer = Login('./zm.txt')
    loginer.try_all()

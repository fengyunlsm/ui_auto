import sys, os
base_path = os.getcwd()
sys.path.append(base_path)
print (base_path)
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time, datetime, os


class SeleniumDriver:
    def __init__(self, browser, node=None):
        self.node = node
        self.driver = self.open_window(browser) 
  
    def open_window(self, browser):
        try:
            if browser == 'chrome':
                if 'linux' in sys.platform:
                    options = webdriver.ChromeOptions()
                    binary_location = '/usr/bin/google-chrome'
                    chrome_driver_binary = '/usr/bin/chromedriver'
                    options.add_argument('--headless')  # 无界面运行 
                    options.add_argument('--no-sandbox') # 以最高权限运行
                    options.add_argument('--start-maximized')   # 最大化运行，设置元素定位比较准确
                    options.add_argument('--disable-gpu')
                    options.add_argument('window-size=1920x3000')
                    options.add_argument('--hide-scrollbars') # 影藏滚动条
                    options.add_argument('blink-settings=imagesEnabled=false') # 不加载图片提升速度
                    # chrome_options.binary_location = binary_location
                    chromedriver = chrome_driver_binary
                    # chrome_options.add_argument('--disable-dev-shm-usage')
                    options.add_argument("service_args=['–ignore-ssl-errors=true', '–ssl-protocol=TLSv1']") 
                    options.add_experimental_option('excludeSwitches', ['enable-automation'])
                    # options = chrome_driver_binary
                    os.environ["webdriver.chrome.driver"] = chromedriver
                    driver = webdriver.Chrome(executable_path = chromedriver, options = options) # 输入参数为options=options
                    # driver.quit()
                    # WAIT = WebDriverWait(driver, 5)
                else:
                    options = webdriver.ChromeOptions()
                    prefs = {'download.default_directory': 'D:\\Download\\', 'profile.default_content_settings.popups': 0} # 设置自定义路径
                    options.add_experimental_option('prefs', prefs) # 设置默认路径
                    driver = webdriver.Chrome(options=options) # 输入参数为options=options
                    return driver
        except:
            return None


    def get_url(self, url):
        if self.driver != None:
            if 'https://' in url:
                self.driver.get(url) # 打开对应的网站
            elif 'http://' in url:
                self.driver.get(url)
            else:
                print("打开地址失败")
        else:
            print("打开地址失败")
        time.sleep(2)
        self.driver.quit()
        

if __name__ == "__main__":
    s = SeleniumDriver("chrome")
    s.get_url("http://www.baidu.com")

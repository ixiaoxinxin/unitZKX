# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Basepage(object):
    '''
    启动默认浏览器：chrome，ie，Firefox
    '''
    def __init__(self,browser = 'ff'):
        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser,You can enter 'ie', 'ff' or 'chrome'." % browser)

    def element_wait(self,secs,by=None, value=None):#没有添加判空的方法
        index = 0
        self.by = by
        self.value = value

        if by == "id":
            WebDriverWait(self.driver,secs,2).until(EC.presence_of_all_elements_located(By.ID,value))
        elif by == "name":
            WebDriverWait(self.driver,secs,2).until(EC.presence_of_all_elements_located(By.NAME,value))
        elif by == "class":
            WebDriverWait(self.driver,secs,2).until(EC.presence_of_all_elements_located(By.CLASS_NAME,value))
        elif by == "link_text":
            WebDriverWait(self.driver,secs,2).until(EC.presence_of_all_elements_located(By.LINK_TEXT,value))
        elif by == "xpath":
            WebDriverWait(self.driver,secs,2).until(EC.presence_of_all_elements_located(By.XPATH,value))
        elif by == "css":
            WebDriverWait(self.driver,secs,2).until(EC.presence_of_all_elements_located(By.CSS_SELECTOR,value))
        else:
            raise NameError("请输入正确的元素类型！")
    def get_element(self,by=None, value=None):#没有添加判空的方法
        index = 0
        self.by = by
        self.value = value
        if by == "id":
            element = self.driver.find_element(value)
        elif by == "name":
            element = self.driver.find_element(value)
        elif by == "class":
            element = self.driver.find_element(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("请输入正确的元素类型！")
        return element

    def open(self,url):
        self.driver.get(url)

    def max_window(self):
        self.driver.maximize_window()

    def set_windows(self,wide,high):
        self.driver.set_window_size(wide,high)

    def type(self,by,value):
        self.element_wait(by)
        cl = self.get_element(value)
        cl.send_keys(value)

    def clear(self,by,value):
        self.element_wait(by)
        cl = self.get_element(value)
        cl.clear()

    def click(self,ele):
        self.element_wait(ele)
        cl = self.get_element(ele)
        cl.click()

if __name__ == '__main__':
    driver = Basepage("ff")







































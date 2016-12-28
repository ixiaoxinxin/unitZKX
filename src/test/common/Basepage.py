from selenium import selenium,webdriver
import time
from time import sleep
import config


class Basepage(object):
    def __init__(self):
        self.webdriver = webdriver

    def my_open_browser(self):
        self.browser = webdriver.Ie(config.IEDriverServer.DRIVER_OF_IE)
        self.url = self.browser.get(config.IEDriverServer.BASE_URL)

        return self.url



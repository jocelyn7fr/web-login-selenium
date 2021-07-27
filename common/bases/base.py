"""
对原始的基本方法的封装
实现步骤
"""
from time import sleep
from selenium import webdriver
from common.bases.print_log import logger
from run_all import img_dir_path
import time

class Base:
    def __init__(self,driver):
        self.driver = driver

    def wait(self,time):
        sleep(time)

    def search_element(self,loc,msg=''):   #对最原始
        logger.info('开始查找页面元素：{}'.format(msg))
        try:
            element = self.driver.find_element(*loc) #传元组类型的数据形式是加*
            logger.info('找到页面元素: {}'.format(msg))
            return element
        except Exception as e:
            self.save_picture(msg)
            print(e)

    def click_element(self, loc, msg=''):
        self.search_element(loc, msg).click()
        logger.info('点击了页面元素：{}'.format(msg))

    def send_data(self, loc, data, msg=''):
        self.search_element(loc, msg).send_keys(data)
        logger.info('向页面元素：{0}发送了数据{1}'.format(msg, data))

    def get_element_text(self,loc,msg=''):
        text = self.search_element(loc,msg).text
        logger.info('获取页面元素文本内容：{}'.format(msg))
        return text

    def save_picture(self, msg=''):
        img_file_path = img_dir_path + '{0}-{1}.png'.format(msg, time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
        try:
            self.driver.save_screenshot(img_file_path)
            logger.info('截图成功，图片保存路径为：{}'.format(img_file_path))
        except Exception as e:
            logger.warn('截图失败：{}'.format(msg))
            print(e)

        

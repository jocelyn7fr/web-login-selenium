"""
执行测试用例之前的调起浏览器操作和测试用例执行完后的关闭浏览器操作
1import pytest
2实现一个装饰器函数handler
"""
import pytest
import os
from pages.login_page import LoginPage
from selenium import webdriver
from test_data.test_data import url
from common.bases.print_log import logger

##os.path.abspath---绝对路径
# chromedriver_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)),'chromedriver.exe'))
## print('chromedriver_path:',chromedriver_path)
driver = None   #定义全局变量


@pytest.fixture(scope='session')  #跨模块调用 模块就是一个文件  此装饰器用做执行测试用例之前的一个初始化
def handler():
    global driver #申明全局变量
    logger.info('开始进行JRJ Web  自动化项目测试')
    # driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver=webdriver.Firefox()
    lp = LoginPage(driver)
    driver.maximize_window()
    driver.get(url)
    lp.wait(3)
    yield lp   #把实例对象lp返回给测试用例
    driver.quit()


@pytest.fixture()
def refresh_page():
    driver.refresh()
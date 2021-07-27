"""
实现登录操作的测试用例
"""
from pages.login_page import LoginPage
from test_data.test_data import test_login_success
from test_data.test_data import test_login_failed
import pytest
import allure
from common.bases.print_log import logger


@allure.epic('JRJ Web 自动化测试项目')
@allure.feature('JRK Web 项目登录模块自动化测试')

#每次用例执行前实行刷新
@pytest.mark.usefixtures('refresh_page')  # 针对没有返回值适合使用usefixtures装饰器
class TestLogin:
    @allure.story('登录模块-正常用例测试')
    @allure.title('登录-正向用例')
    @pytest.mark.last  #项目必须有pytest-ordering的包
    def test_login_success(self,handler): #传入handler---执行测试用例之前调起浏览器
        logger.info('----------开始执行正向用例测试------------')
        with allure.step('开始执行登录操作'):
            allure.attach(f'发送用户名：{test_login_success["username"]}')
            allure.attach(f'发送密码：{test_login_success["password"]}')
            allure.attach('点击登录')
        handler.login(test_login_success['username'], test_login_success['password'])
        # assert test_login_success['msg'] == handler.get_logout_text('退出文本')
        assert '财友0r390j8p' == handler.get_username('用户名')

    @allure.story('登录模块-反向用例测试')
    @allure.title('登录-反向用例')
    @pytest.mark.parametrize('data', test_login_failed)
    def test_login_failed(self, handler, data):   #data是代表列表test_login_failed中的每条数据的参数
        logger.info('-----------开始执行反向用例测试------------')
        with allure.step('开始执行登录操作'):
            allure.attach(f'发送用户名：{data["username"]}')
            allure.attach(f'发送密码：{data["password"]}')
            allure.attach('点击登录')
        handler.login(data['username'], data['password'])
        if data['username'] == '' or data['password'] == '':
            assert data['error_msg'] == handler.get_free_reg('获取免费注册文本')
        else:
            assert data['error_msg'] == handler.get_account_passwd_wrong_text('获取账号或密码错误文本')

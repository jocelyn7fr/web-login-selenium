"""
对登录页面，页面元素操作方法的实现
1导入父类Base和 LoginLocator
2建立子类
3实现子类的登录方法
"""
from common.bases.base import Base
from locators.login_locator import LoginLocator



class LoginPage(Base):  #继承了Base
    def login(self, username, password):
        self.send_data(LoginLocator.username_input_loc, username,'用户输入框')
        self.send_data(LoginLocator.password_input_loc, password,'密码输入框')
        self.click_element(LoginLocator.login_btn_loc,'登录按钮')
        self.wait(3)


    def get_logout_text(self, msg=''):
        return self.get_element_text(LoginLocator.logout_text_loc, msg)

    def get_username(self, msg=''):
        return self.get_element_text(LoginLocator.username_loc, msg)

    def get_free_reg(self, msg=''):
        """
        获取免费注册文本
        :param msg: 对’免费注册‘文本的说明
        :return: 文本内容：‘免费注册'
        """
        return self.get_element_text(LoginLocator.free_register_loc, msg)

    def get_account_passwd_wrong_text(self, msg=''):
        """
        获取账号或密码错误提示文本
        :param msg: 对提示文本的说明
        :return: 返回'账号或密码错误'
        """
        return self.get_element_text(LoginLocator.account_passwd_wrong_loc, msg)
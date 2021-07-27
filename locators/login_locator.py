"""

"""
from selenium.webdriver.common.by import By
#对定位方法的封装


# class LoginLocator:
#     username_input_loc = (By.ID,'txtUsername') #定位用户名输入框
#     password_input_loc = (By.ID,'txtPassword')
#     login_btn_loc =(By.CLASS_NAME,'sso-btn-login')
#     free_register_loc = (By.LINK_TEXT,'免费注册')
#     account_passwd_wrong_loc = (By.XPATH, '//span[contains(text(), "账号或密码错误")]')
#     logout_text_loc = (By.ID,'logout_ok')  #定位登出文本 退出
#     username_loc = (By.LINK_TEXT,'财友0r390j8p')
class LoginLocator:
    username_input_loc = (By.ID, 'txtUsername')
    password_input_loc = (By.ID, 'txtPassword')
    login_btn_loc = (By.CLASS_NAME, 'sso-btn-login')
    free_register_loc = (By.LINK_TEXT, '免费注册')
    account_passwd_wrong_loc = (By.XPATH, '//span[contains(text(), "账号或密码错误")]')
    logout_text_loc = (By.ID, 'logout_ok')
    username_loc = (By.LINK_TEXT, '财友0r390j8p')
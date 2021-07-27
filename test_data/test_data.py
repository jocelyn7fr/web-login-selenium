"""
存放测试数据
"""
url = 'https://sso.jrj.com.cn/sso/ssopassportlogin'

test_login_success = {'name': '登录正向用例', 'username': '财友0r390j8p', 'password': 'ff970227', 'msg': '退出'}

test_login_failed = [
    {'name': '登录反向用例-用户名为空', 'username': '', 'password': 'ff970227', 'error_msg': '免费注册'},
    {'name': '登录反向用例-用户名错误', 'username': '财友', 'password': 'ff970227', 'error_msg': '账号或密码错误'},
    {'name': '登录反向用例-密码为空', 'username': '财友0r390j8p', 'password': '', 'error_msg': '免费注册'},
    {'name': '登录反向用例-密码错误', 'username': '财友0r390j8p', 'password': '123456', 'error_msg': '账号或密码错误'}
                     ]
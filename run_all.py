"""
运行所有测试用例的入口
"""

import pytest
from common.bases.read_config import read_config
import os
import sys

BASE_DIR = os.path.dirname('__file__')
config_file_path = os.path.join(BASE_DIR,'common/config/config.ini')
test_results_dir_path = read_config(config_file_path, 'report', 'allure_results_dir_path')
test_report_dir_path = read_config(config_file_path, 'report', 'test_report_dir_path')
img_dir_path = read_config(config_file_path, 'img', 'img_dir_path')

if __name__ == '__main__':
    args = ['-s','-q','--alluredir', test_results_dir_path]
    #通过关键字运行指定的测试用例
    self_args = sys.argv[1:]
    all_args = args + self_args
    pytest.main(all_args)   #获取在运行配置里写的参数 (可以选择只运行哪一条用例）
    # pytest.main(args)
    cmd = 'allure generate %s -o %s -c' % (test_results_dir_path, test_report_dir_path) #-o代表operate 输出
    os.system(cmd)


"""
读取配置文件内容
1import configparser
2写个函数实现读取配置文件内容
3将读取到的内容返回给函数
"""
import sys
import configparser
from common.bases.print_log import logger
import os
#根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# print('Base_dir:',BASE_DIR)

def read_config(config_file_path,field,key):  #相当于config_file_path=配置文件路径,field=[img],key=img_dir_path
    cf = configparser.ConfigParser()  #cf做了个实例化
    try:
        cf.read(config_file_path,encoding='utf-8')
        result = cf.get(field,key).replace('base_dir',BASE_DIR).replace('\\','/')
        if ':' in result:
            result = cf.get(field,key).replace('base_dir',BASE_DIR).replace('/','\\') #替换windows路劲下的分隔符


    except Exception as e:
        logger.error(e)    #将错误相关信息打印出来
        sys.exit(1)   #异常退出
    return result
if __name__ == '__main__':
    config_file_path = os.path.join(BASE_DIR,'common/config/config.ini')
    img_dir_path = read_config(config_file_path,'img','img_dir_path')
    allure_results_dir_path = read_config(config_file_path,'report','allure_results_dir_path')
    print('img_dir_path:',img_dir_path)
    print('allure_results_dir_path:',allure_results_dir_path)

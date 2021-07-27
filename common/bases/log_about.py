"""
日志控制输出
1导入logging
2调用basicconfig方法控制日志输出的等级
"""

import logging
logging.basicConfig(level=logging.ERROR)

logging.debug('this is debug message!')
logging.info('this is info message!')
logging.warning('this is warning message!')
logging.error('this is error message!')
logging.critical('this is critical message!')
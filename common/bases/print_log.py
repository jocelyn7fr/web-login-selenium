"""
打印日志功能
1import logging
2写一个日志打印功能，按一定格式输出

"""
import logging

def p_log():
    logging.basicConfig(level=logging.INFO,format='%(name)s - %(asctime)s - %(filename)s - [line:%(lineno)d -'
                                                  ' %(levelname)s: %(message)s')
    getlog = logging.getLogger('jrj_web_autotest_25')
    return getlog

logger = p_log()

if __name__ == '__main__':
    logger.info('info message test.')
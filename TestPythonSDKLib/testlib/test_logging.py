import logging

import sys
from logging import handlers


def get_logger(filename, log_level=logging.INFO):

    # 创建日志对象
    log = logging.getLogger(filename)

    # 设置日志级别
    log.setLevel(log_level)

    # 日志输出格式
    fmt = logging.Formatter('%(asctime)s %(thread)d %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    # 输出到控制台
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(fmt)

    # 输出到文件

    # 日志文件按天进行保存，每天一个日志文件
    file_handler = handlers.TimedRotatingFileHandler(filename=filename, when='D', backupCount=1, encoding='utf-8')

    # 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件
    # file_handler = handlers.RotatingFileHandler(filename=filename, maxBytes=1*1024*1024*1024, backupCount=1, encoding='utf-8')
    file_handler.setFormatter(fmt)

    log.addHandler(console_handler)
    log.addHandler(file_handler)

    return log


if __name__ == '__main__':

    # 指定日志输出的文件路径 和 日志级别
    logger = get_logger('./logs/log.txt', logging.DEBUG)
    logger.debug('日志输出测试')



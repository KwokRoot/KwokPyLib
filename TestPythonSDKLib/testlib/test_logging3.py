import logging

if __name__ == '__main__':

    LOG_FORMAT = '%(asctime)s %(thread)d %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'

    # 默认情况下 python 的 logging 模块将日志打印到了标准输出中，且只显示了大于等于 WARNING 级别的日志
    # 默认的日志级别为 WARNING（日志级别等级 FATAL(CRITICAL) > ERROR > WARNING(WARN) > INFO > DEBUG > NOTSET）
    # 默认的日志格式为：日志级别:Logger名称:输出消息。
    # logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')


import logging
import os


def get_logger(filename, log_level=logging.INFO):
    if os.path.exists(filename):
        mode = 'a'
    else:
        mode = 'w'

    logging.basicConfig(
        level=log_level,
        format='%(asctime)s %(thread)d %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
        filename=filename,
        filemode=mode
    )
    return logging


if __name__ == '__main__':
    current_path = os.getcwd()
    path = os.path.join(current_path, "logs", 'log.txt')
    log = get_logger(path, logging.DEBUG)

    log.info('info')
    log.warning('warning')
    log.error('error')
    log.debug('debug')


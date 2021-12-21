import logging
import os
from datetime import datetime

def set_logger():
    dt_now = datetime.now()
    date = dt_now.strftime('%Y-%m-%d')

    logger_name = "example"
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # create file handler
    module_path = os.path.dirname(__file__)
    module_path = module_path + '/../log/' + date + '.log'
    fh = logging.FileHandler(module_path)
    fh.setLevel(logging.INFO)

    # create formatter
    fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    # datefmt = "%a %d %b %Y %H:%M:%S"
    formatter = logging.Formatter(fmt)

    # add handler and formatter to logger
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
logger = set_logger()


import logging
from logging.config import fileConfig

fileConfig('logging_config1.ini')
logger = logging.getLogger()
logger.debug('often makes a very good meal of %s', 'visiting tourists')

def myFn():
    logger.debug('hello logging in function ')
    pass

myFn()

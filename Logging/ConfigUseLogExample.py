import logging
from logging.config import fileConfig

fileConfig('config.ini')
logger = logging.getLogger()
logger.info('\n Am in logger.info statement')
logger.debug('Often makes a very good meal of %s','visiting Tourist')

def myFn():
    logger.debug('Hello... We are inside myFn() now...')
    pass

myFn()

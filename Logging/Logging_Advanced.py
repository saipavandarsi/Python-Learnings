import Logging

logger = Logging.getLogger(__name__)
logger.setLevel(Logging.INFO)


#create a file handler
handler = Logging.FileHandler('hello.log')
handler.setLevel(Logging.INFO)

#create a logging format
formatter = Logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the haandler to the logger
logger.addHandler(handler)

logger.info('Hello Shruthi')
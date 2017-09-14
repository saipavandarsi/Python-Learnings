import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Start Reading Database')

#read Database here
records = {'Shruthi':111, 'Pavan':222}

logger.debug('Reacords : %s',records)
logger.info('Updating Records')

#update records here
logger.info('Records Updated')

logger.warn('close DB Connection')
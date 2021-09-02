from utils import logger
log = logger.setup_applevel_logger(file_name = 'app_debug.log')

from mymodule import multiply as mt

log.debug('Calling module function.')
x  = mt.multiply(3,4)
log.debug('Finished.')
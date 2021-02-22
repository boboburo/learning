#!/bin/python3

LOGGER_LEVEL = "INFO"
FH_LEVEL = "INFO"
CH_LEVEL = "DEBUG"

#to do implement this in nicer json ? 
#add a decorator for time ? 

"""
from bc_logger import get_logger
logger = get_logger(__name__) 
"""


import logging
from logging.handlers import TimedRotatingFileHandler

def get_logger(name):

    file_formatter = logging.Formatter('time:%(asctime)s~level:%(levelname)s~module:%(module)s~function:%(funcName)s~message:%(message)s')
    console_formatter = logging.Formatter('%(levelname)s -- %(message)s')
    
    file_handler = TimedRotatingFileHandler("j2p_log_version_021.log", when = "d",interval=1)
    file_handler.setLevel(logging.FH_LEVEL)
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.CH_LEVEL)
    console_handler.setFormatter(console_formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.LOGGER_LEVEL)

    if not logger.handlers: #need this to control function is called from another place 
        logger.addHandler(file_handler)
        #logger.addHandler(console_handler)

    
    return logger
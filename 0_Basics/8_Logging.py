#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# +++++++++ Logging +++++++++
# logging.basicconfig(filename='txt.txt') - defines the file where you want to log, instead of screen
# ===================================================================================================

# add the following at the beginning of the program
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
# logging.disable(logging.DEBUG) - uncomment this if you want to disable logging

# then everywhere you need to print something use
k = 100
logging.debug('This variabel is {}'.format(k))
logging.debug('Hello')
logging.debug(str(k)+ ' This message')

# then, when you are done you will disable logging
logging.disable(logging.DEBUG)

# there are multiple levels
# DEBUG - lowest level
# INFO - general events
# WARNING - non critical problems that do not prevent program from stopping
# ERROR - error that caused the program to stop doing something
# CRITICAL - fatal errors
# logging.disable() - will disable all logging
# ===================================================================================================

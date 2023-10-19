import logging  
import logging.handlers


# logger creation 
logger = logging.getLogger('my logger')
# set message format (see https://docs.python.org/3/library/logging.html for format syntax)
formatter = logging.Formatter("[%(name)s %(levelname)s]-%(asctime)s %(message)s","%Y-%m-%d %H:%M:%S") 
# file handler
fileHandler = logging.handlers.RotatingFileHandler('myserver.log', maxBytes=1024, backupCount=3)
fileHandler.setFormatter(formatter)

# console output handler
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)

# attach handler to logger
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

logger.setLevel(logging.DEBUG) # by default warning is the lowest (CRITICAL 50, ERROR 40, WARNING 30, INFO 20, DEBUG 10)

def logger_test(msg):
    logger.error(f"error {msg}")
    logger.warning(f"warning {msg}")
    logger.info(f"info {msg}")
    logger.debug(f"debug {msg}")
 
if __name__ == "__main__":   
    i = 1
    logger_test(f"msg {i}")
    # change level
    print("Let us change the level")
    logger.setLevel(logging.WARNING)
    i = 2
    logger_test(f"msg {i}")




import logging
def ex():
    logger.critical("this is a critical")
    logger.error("this is an error")
    logger.warning("this is a warning")
    logger.info("this is a logger")
    logger.debug("this is a debug")

logger=logging.getLogger("logger_ex")
ex()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
ex()
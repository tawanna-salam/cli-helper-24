import logging
from logging.handlers import RotatingFileHandler

# Set up logging configuration
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_FILE = 'app.log'

# Create a logger
logger = logging.getLogger('cli-helper-24')
logger.setLevel(logging.DEBUG)

# Set up rotation handler
handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=2)
handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Add the handler to the logger
logger.addHandler(handler)

# Example usage of logger
if __name__ == '__main__':
    logger.debug('This is a debug message')
    logger.info('Informational message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')

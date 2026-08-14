import logging
from logging.handlers import RotatingFileHandler

# Configure logger for the application

def setup_logger(log_file='app.log', max_bytes=5 * 1024 * 1024, backup_count=3):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

# Example usage of the logger
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger initialized successfully.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')

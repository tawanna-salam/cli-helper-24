import logging  
import os  
from logging.handlers import RotatingFileHandler  

# Logger configuration function  
def setup_logger(log_file='app.log',  
                log_level=logging.DEBUG,  
                max_bytes=5 * 1024 * 1024,  
                backup_count=3):  
    # Create a logger  
    logger = logging.getLogger(__name__)  
    logger.setLevel(log_level)  

    # Create a rotating file handler  
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)  
    handler.setLevel(log_level)  

    # Create a logging format  
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
    handler.setFormatter(formatter)  

    # Add the handler to the logger  
    logger.addHandler(handler)  
    return logger  

# Example usage  
if __name__ == '__main__':  
    log = setup_logger()  
    log.info('Logger setup complete.')  
    log.warning('This is a warning message.')  
    log.error('This is an error message.')  

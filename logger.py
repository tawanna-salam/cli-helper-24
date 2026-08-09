import logging

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warn(self, message):
        self.logger.warning(message)

    def debug(self, message):
        self.logger.debug(message)

# Example usage
if __name__ == '__main__':
    log = Logger('cli-helper-24')
    log.info('This is an info message')
    log.debug('This is a debug message')
    log.warn('This is a warning message')
    log.error('This is an error message')
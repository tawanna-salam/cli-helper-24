import logging

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


def debug(message):
    """Log a message with DEBUG level."""
    logger.debug(message)


def info(message):
    """Log a message with INFO level."""
    logger.info(message)


def warning(message):
    """Log a message with WARNING level."""
    logger.warning(message)


def error(message):
    """Log a message with ERROR level."""
    logger.error(message)


def critical(message):
    """Log a message with CRITICAL level."""
    logger.critical(message)


def set_level(level):
    """Set the logging level based on user input."""
    level_dict = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    logger.setLevel(level_dict.get(level.upper(), logging.INFO))

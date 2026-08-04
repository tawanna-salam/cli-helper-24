TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

STATUS_ACTIVE = 'active'
STATUS_INACTIVE = 'inactive'
STATUS_PENDING = 'pending'

ERROR_CODE_NOT_FOUND = 404
ERROR_CODE_SERVER_ERROR = 500

DEFAULT_PAGE_SIZE = 20
DEFAULT_TIMEOUT = 30

LOG_LEVEL_DEBUG = 'DEBUG'
LOG_LEVEL_INFO = 'INFO'
LOG_LEVEL_WARNING = 'WARNING'
LOG_LEVEL_ERROR = 'ERROR'

API_BASE_URL = 'https://api.example.com/v1/' 

SUPPORTED_FILE_EXTENSIONS = ['.txt', '.csv', '.json', '.xml']

def get_status_codes():
    return {
        'active': STATUS_ACTIVE,
        'inactive': STATUS_INACTIVE,
        'pending': STATUS_PENDING
    }

def get_log_levels():
    return {
        'debug': LOG_LEVEL_DEBUG,
        'info': LOG_LEVEL_INFO,
        'warning': LOG_LEVEL_WARNING,
        'error': LOG_LEVEL_ERROR
    }
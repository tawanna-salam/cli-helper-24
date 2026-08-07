import re

def is_valid_email(email):
    """Check if the provided email is valid."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def is_positive_integer(value):
    """Check if the value is a positive integer."""
    if isinstance(value, int) and value > 0:
        return True
    return False


def is_valid_url(url):
    """Check if the provided URL is valid."""
    url_regex = r'^(https?|ftp)://[\w.-]+(:\d+)?(/[\w.-]*)*$'
    return re.match(url_regex, url) is not None


def is_non_empty_string(value):
    """Check if the value is a non-empty string."""
    return isinstance(value, str) and len(value) > 0


def is_in_range(value, min_value, max_value):
    """Check if the value is within a specified range."""
    return min_value <= value <= max_value

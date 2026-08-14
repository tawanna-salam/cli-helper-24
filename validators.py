def validate_username(username):
    if not isinstance(username, str):
        raise TypeError("Username must be a string.")
    if len(username) < 3:
        raise ValueError("Username must be at least 3 characters long.")
    if len(username) > 20:
        raise ValueError("Username must be no more than 20 characters long.")
    if not username.isalnum():
        raise ValueError("Username can only contain alphanumeric characters.")
    return True


def validate_game_score(score):
    if not isinstance(score, int):
        raise TypeError("Score must be an integer.")
    if score < 0:
        raise ValueError("Score cannot be negative.")
    return True


def validate_level(level):
    if not isinstance(level, int):
        raise TypeError("Level must be an integer.")
    if level < 1:
        raise ValueError("Level must be at least 1.")
    return True


def validate_email(email):
    if not isinstance(email, str):
        raise TypeError("Email must be a string.")
    if "@" not in email or len(email.split("@")) != 2:
        raise ValueError("Email must contain a single '@' character.")
    return True
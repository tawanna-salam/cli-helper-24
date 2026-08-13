def validate_username(username):
    if not isinstance(username, str):
        raise ValueError('Username must be a string.')
    if len(username) < 3 or len(username) > 20:
        raise ValueError('Username must be between 3 and 20 characters.')
    if not username.isalnum():
        raise ValueError('Username must be alphanumeric.')
    return True


def validate_score(score):
    if not isinstance(score, int):
        raise ValueError('Score must be an integer.')
    if score < 0:
        raise ValueError('Score cannot be negative.')
    return True


def validate_level(level):
    if not isinstance(level, int):
        raise ValueError('Level must be an integer.')
    if level < 1:
        raise ValueError('Level must be at least 1.')
    return True


def validate_input(data):
    try:
        validate_username(data['username'])
        validate_score(data['score'])
        validate_level(data['level'])
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'success', 'message': 'Input is valid.'}
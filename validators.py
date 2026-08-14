def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    if len(user_input) > 100:
        raise ValueError('Input exceeds maximum length of 100 characters')
    return True

def validate_score(score):
    if not isinstance(score, int):
        raise TypeError('Score must be an integer')
    if score < 0:
        raise ValueError('Score cannot be negative')
    if score > 100:
        raise ValueError('Score cannot exceed 100')
    return True

# Example usage
try:
    validate_input('')  # This should raise an error
except ValueError as e:
    print(f'Input validation error: {e}')

try:
    validate_score(150)  # This should raise an error
except ValueError as e:
    print(f'Score validation error: {e}')
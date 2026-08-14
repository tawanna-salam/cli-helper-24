import sys

class InputError(Exception):
    pass

def validate_input(user_input):
    if not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 10:
        raise InputError('Input must be a number between 1 and 10.')
    return int(user_input)

def main():
    while True:
        user_input = input('Enter a number between 1 and 10 (or type exit to quit): ').strip()
        if user_input.lower() == 'exit':
            print('Exiting the program. Goodbye!')
            break
        try:
            validated_input = validate_input(user_input)
            print(f'You entered: {validated_input}')
        except InputError as e:
            print(e)

if __name__ == '__main__':
    main()
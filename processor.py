import sys
import re

# Function to validate user input
def validate_input(user_input):
    if not user_input:
        return False, 'Input cannot be empty.'
    if not re.match('^[a-zA-Z0-9_]+$', user_input):
        return False, 'Input can only contain alphanumeric characters and underscores.'
    return True, ''

# Main processing loop
def main_loop():
    while True:
        user_input = input('Enter a command (or type "exit" to quit): ')
        valid, message = validate_input(user_input)
        if user_input.lower() == 'exit':
            print('Exiting program.')
            break
        if not valid:
            print(f'Error: {message}')
            continue
        print(f'You entered a valid command: {user_input}')

if __name__ == '__main__':
    main_loop()
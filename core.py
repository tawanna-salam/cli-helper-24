import sys


def process_input(user_input):
    if not user_input:
        raise ValueError("Input cannot be empty")
    if not user_input.isalpha():
        raise ValueError("Input must contain only letters")
    return user_input


def main():
    while True:
        try:
            user_input = input('Enter a string: ')
            valid_input = process_input(user_input)
            print(f'You entered a valid string: {valid_input}')
            break
        except ValueError as e:
            print(f'Error: {e}. Please try again.')


if __name__ == '__main__':
    main()
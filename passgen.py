import pyperclip
import random


letters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
numbers = '0123456789'
special = '!@#$%^&*()_+[]{}:;\'"<>,.\\/?`~'

num_letters = 11
num_numbers = 10
num_special = 11

password = []


def populate_string(string, symbols, num_symbols):
    for _ in range(num_symbols):
        current_char = random.choice(symbols)
        string.append(current_char)


populate_string(password, letters, num_letters)
populate_string(password, numbers, num_numbers)
populate_string(password, special, num_special)

random.shuffle(password)
password = ''.join(password)
pyperclip.copy(password)
print('The password has been copied to the clipboard.')

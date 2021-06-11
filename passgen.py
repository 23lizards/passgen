import pyperclip
import random


letters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
numbers = '0123456789'
special = '!@#$%^&*()_+[]{}:;\'"<>,.\\/?`~'

num_letters = 11
num_numbers = 10
num_special = 11

password = []

for _ in range(num_letters):
    current_char = random.choice(letters)
    password.append(current_char)

for _ in range(num_numbers):
    current_char = random.choice(numbers)
    password.append(current_char)

for _ in range(num_special):
    current_char = random.choice(special)
    password.append(current_char)

random.shuffle(password)
password = ''.join(password)
pyperclip.copy(password)
# The password has now been copied to your clipboard.

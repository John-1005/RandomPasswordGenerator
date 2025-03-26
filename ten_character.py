
import random
import string

upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case_letters = "abcdefghjijkmnopqrstuvwxyz"
numbers = "1234567890"
special_character = "!@#$%^&*?"

def ten_character_password(length):
    temp_lower = random.sample(lower_case_letters, 10)
    password = "".join(temp_lower)
    print(f"Your password is {password}")

def ten_capital_character_password(length):
    temp_lower = random.sample(lower_case_letters, 8)
    temp_upper = random.sample(upper_case_letters, 2)
    temp_password = temp_lower + temp_upper
    mix_password = random.sample(temp_password, 10)
    password = "".join(mix_password)
    print(f"Your capital password is: {password}")

def ten_number_character_password(length):
    temp_lower = random.sample(lower_case_letters, 8)
    temp_number = random.sample(numbers, 2)
    temp_password = temp_lower + temp_number
    mix_password = random.sample(temp_password, 10)
    password = "".join(mix_password)
    print(f"Your password is: {password}")
    
def ten_special_character_password(length):
    temp_lower = random.sample(lower_case_letters, 8)
    temp_special = random.sample(special_character, 2)
    temp_password = temp_lower + temp_special
    mix_password = random.sample(temp_password, 10)
    password = "".join(mix_password)
    print(f"Your password is: {password}")

def ten_capital_number_password(length):
    temp_lower = random.sample(lower_case_letters, 6)
    temp_upper = random.sample(upper_case_letters, 2)
    temp_number = random.sample(numbers, 2)
    temp_password = temp_lower + temp_upper + temp_number
    mix_password = random.sample(temp_password, 10)
    password = "".join(mix_password)
    print(f"Your password is: {password}")

def ten_capital_special_password(length):
    temp_lower = random.sample(lower_case_letters, 6)
    temp_upper = random.sample(upper_case_letters, 2)
    temp_special = random.sample(special_character,2 )
    temp_password = temp_lower + temp_upper + temp_special
    mix_password = random.sample(temp_password, 10)
    password = "".join(mix_password)
    print(f"Your password is: {password}")

def ten_number_special_password(length):
    temp_lower = random.sample(lower_case_letters, 6)
    temp_number = random.sample(numbers, 2)
    temp_special = random.sample(special_character, 2)
    temp_password = temp_lower + temp_number + temp_special
    mix_password = random.sample(temp_password, 10)
    password = "".join(mix_password)
    print(f"Your password is: {password}")

def ten_full_character_password(length):
    temp_lower = random.sample(lower_case_letters, 5)
    temp_number = random.sample(numbers, 2)
    temp_upper = random.sample(upper_case_letters, 2)
    temp_special = random.sample(special_character, 1)
    temp_password = temp_lower + temp_number + temp_upper + temp_special
    mix_password = random.sample(temp_password, 10)
    password = "".join(mix_password)
    print(f"Your password is: {password}")

def eleven_character_password(length):
    temp_lower = random.sample(lower_case_letters, 11)
    password = "".join(password_letters)
    print(f"Your password is {password}")

def twelve_character_password(length):
    temp_lower = random.sample(lower_case_letters, 12)
    password = "".join(temp_lower)
    print(f"Your password is {password}")


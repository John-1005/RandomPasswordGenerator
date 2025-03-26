#Random Password Generator
#Needs to randomly choose between random x number of characters
#Characters can be Upper and lowercase letters, certain special characters and numbers
#Figure out how to combine all those choices, can be random or cactonized if so numbers need to be strings
#After all the choices the program needs to randomly choose and combine all characters
#Possibly create multiple functions for choosing the letters, special characters and numbers
#Then create the final function that combines them all and returns the password?
#How do I make it so I don't need many if statements inside if statements
#Example if they want 8 characters and only capitals and lower, or 8 characters and lower with numbers
#Can do something with the sample(x, length), length = x to make choosing for 8-12 better

from ten_character import *
from eleven_character import *
from twelve_character import *
import random
import string
upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case_letters = "abcdefghjijkmnopqrstuvwxyz"
numbers = "1234567890"
special_character = "!@#$%^&*?"

def main():
    length = int(input("Please enter the number for the length of the password between 10-12 characters: "))
    capital_letter = input("Do you want capital letters, Yes or No: ").lower().strip()
    number = input("Do you want numbers, Yes or No: ").lower().strip()
    special = input("Do you want special characters, Yes or No: ").lower().strip()

    if length == 10:
        if capital_letter == "yes":
            if number == "yes":
                if special == "yes":
                    return ten_full_character_password(length)
                else:
                    return ten_capital_number_password(length)
            else:
                return ten_capital_character_password(length)

        elif number == "yes":
            
            if special == "yes":

                return ten_number_special_password(length)

            else:
                return ten_number_character_password(length)

        elif special == "yes":
            return ten_special_character_password(length)

        else:
            return ten_character_password(length)
    if length == 11:
        eleven_character_password(length)
    if length == 12:
        twelve_character_password(length)
"""
    while True:
        try:
            length = int(input("Please enter the a number for the length of the password between 10-12 characters: "))
            if length < 10 or length > 12:
                print(f"Invalid Choice!!")
            return length
        except ValueError:
            print("Please enter a valid number")
"""

main()

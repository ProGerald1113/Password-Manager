#importing the random and string
import random
import string


def characters_check(letters_list):
     length = 15
     selected_few = random.choices(letters_list,k=length)
     random.shuffle(selected_few)

     return "".join(selected_few)

def numbers_check(numbers_list):
     length = 3
     numbers_select = random.choices(numbers_list,k = length)
     random.shuffle(numbers_select)
     return int("".join(map(str,numbers_select)))

def symbols_check(symbols_list):
     length = 2
     one_symbol = random.choices(symbols_list,k=length)
     random.shuffle(one_symbol)
     return "".join(one_symbol)

def password_output(letters,numbers,symbols):
     password = list(letters) + list(str(numbers)) + list(symbols)
     random.shuffle(password)
     return "".join(password)

characters = list(string.ascii_letters)
numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ["!","@","?","&","£","#"]

letters = characters_check(characters)
nums = numbers_check(numbers)
symbs = symbols_check(symbols)

password = password_output(letters,nums,symbs)

print(f"Here is your password: {password}")


     

from password_generator import generate
import time
import os 
import json
from datetime import datetime,timedelta,date
from rich.layout import Layout
from rich.console import Console
from rich.text import Text
from cryptography.fernet import Fernet , MultiFernet

key = Fernet.generate_key()

f = Fernet(key)
      

console = Console(style="bold ")
header = Layout(name="header",size=3)
other_Stuff = Layout(name = "footer",size=10)

Date = datetime.now()
expiry = Date + timedelta(days=60) 

actual_Date = Date.strftime("%d-%m-%Y")
actual_Expiry = expiry.strftime("%d-%m-%Y")

path = "Passwords.txt"

if os.path.exists(path):
    pass

else:
    console.print("Necessary requirements have not been met fixing issues...")
    
    time.sleep(1)
    
    console.print("Issues fixed now running")
    time.sleep(1)
    
    with open(path,"w") as file:
        pass

def file_writer(original_filename,info,encrypted_file):
    original_file = open(original_filename, "a+")
    original_file.writelines(info) 

    with open(encrypt_filename, "wb") as encrypted_file:
        text = original_file.read()
        encrypted_data = f.encrypt(text.encode())
        encrypted_file.write(encrypted_data)
        
def file_reader(encrypted_file):
        file = open(encrypted_file,"rb")
        data = file.read()
        decryted_data = f.decrypt(data)
        print(decryted_data)
        

Running = True
password_output = generate()
Original_file = "Passwords.txt"
encrypt_filename = "Passwords_encrypted.txt"

while Running:

    console.print("Welcome to your password manager!!!")
    
    console.print("Press 1 to start the process of creating a password")
    console.print("Press 2 to see your stored passwords")
    console.print("Press 3 to quit")
    
    choice = console.input("Choose an option:")


    if choice == "1":

        console.print("What is your password being used for?")

        console.print("Sidenote: if you dont't wish to specify leave blank")

        usage = console.input("Write here what its being used for:")

        General_info = ("Password:  " , password_output , "  Usage:  "  , usage , "  Created:  " , actual_Date , "  Expiry:  " , actual_Expiry)
        
        file_writer(Original_file,General_info,encrypt_filename)

 
    elif choice == "2":

        if os.stat(encrypt_filename).st_size == 0:
            console.print("Currently there are no saved passwords.")
        else:
            file_reader(encrypt_filename)


    elif choice == "3":
        Running = False
        console.print("Byee!!!")
    
    else:
        console.print("Invalid Option")


    



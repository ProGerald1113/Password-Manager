from password_generator import generate
import time
import os 
import csv
from datetime import timedelta, date
from rich.layout import Layout
from rich.console import Console
from rich.text import Text


console = Console(style="bold ")
header = Layout(name="header",size=3)
other_Stuff = Layout(name = "footer",size=10)

current_date = []
test_date = date.today()
expiry = test_date + timedelta(days=60)
current_date.append(test_date)

path = "Passwords.csv"
if os.path.exists(path):
    pass

else:
    console.print("Necessary requirements have not been met fixing issues...")
    
    time.sleep(1)
    
    console.print("Issues fixed now ready for use!")
    
    time.sleep(1)
    
    with open(path ,"w") as file:
        fieldnames = ["Password " " Used for " " Creation Date " " Expiry Date"]
        password_writer = csv.DictWriter(file, fieldnames=fieldnames)
        password_writer.writeheader()
        

def file_writer(filename,info):
    with open(filename, "w") as file:
        fieldnames = ["Password " " Used for "  " Creation Date "  " Expiry Date"]
        password_writer = csv.DictWriter(file, fieldnames=fieldnames)
        password_writer.writeheader()
        password_writer.writerow(info)
        

def file_reader(file):
    with open(file, "r") as file:
        password_reader = csv.DictReader(file)
        for row in password_reader:
            print(row)

Running = True
password_output = generate()
info = []
file = "Passwords.csv"

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
        
        details = {"password":list(password_output),"Usage":list(usage),"date":current_date,"Expiry":list(expiry)}
        info.append(details)
        file_writer(file,info)
    
    elif choice == "2":
        if os.stat(file).st_size == 0:
            console.print("Currently there are no saved passwords.")
        else:
            file_reader(file)


    elif choice == "3":
        Running = False
        console.print("Byee!!!")
    
    else:
        console.print("Invalid Option")


    



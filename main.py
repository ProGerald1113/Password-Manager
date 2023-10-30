from password_generator import generate
import os 
import csv
from datetime import*

date = date.today()
expiry = date + timedelta(days=60) 

path = "Passwords.csv"
if os.path.exists(path):
    pass

else:
    print("necessary requirements have not been met fixing issues...")
    with open(path ,"w") as file:
        fieldnames = ["Password ", " used for " " Creation Date ",  " Expiry Date"]
        password_writer = csv.DictWriter(file, fieldnames=fieldnames)
        password_writer.writeheader()
        

def file_writer(filename,info):
    with open(filename, "w") as file:
        fieldnames = ["Password ", " used for " , " Creation Date ",  "Expiry Date"]
        password_writer = csv.DictWriter(file, fieldnames=fieldnames)
        password_writer.writeheader()
        password_writer.writerows(info)
        

def file_reader(file):
    with open("Passwords.csv", "r") as file:
        password_reader = csv.DictReader(file)
        for row in password_reader:
            print(row)

Running = True
password_output = generate()
info = []
file = "Passwords.csv"

while Running:

    print("Welcome to your password manager!!!")
    print("Press 1 to start the process of creating a password")
    print("Press 2 to see your stored passwords")
    print("Press 3 to quit")
    
    choice = input("Choose an option:")

    if choice == "1":
        print("What is your password being used for?")
        print("Sidenote: if you dont't wish to specify press 2 ")

        usage = input("Write here what its being used for:")
        details = {"password":password_output,"Usage":usage,"date":date,"Expiry":expiry}
        result = list(info.append(details))
        file_writer(file,result)



    



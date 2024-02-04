from password_generator import generate
import time
import os 
import hashlib
import base64
from datetime import datetime,timedelta,date
from cryptography.fernet import Fernet


Date = datetime.now()
expiry = Date + timedelta(days=60) 

actual_Date = Date.strftime("%d-%m-%Y")
actual_Expiry = expiry.strftime("%d-%m-%Y")

path = "info_encrypted.txt"
login = "login.txt"

if os.path.exists(path):
    pass

else:
    print("Necessary requirements have not been met fixing issues...")
    
    time.sleep(1)
    
    print("Issues fixed now running")
    time.sleep(1)
    
    with open(path,"w") as file:
        pass

def gen_fernet_key(passcode: bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    hlib.update(passcode)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))
        

def file_writer(info,encrypted_file):
     with open(encrypted_file, "ab+") as _file:
        info_Encrypt = f.encrypt(str(info).encode())
        _file.write(info_Encrypt)

def file_reader(encrypted_file):
        with open(encrypted_file,"rb") as file:
            data = file.readline()
            decryted_data = f.decrypt(data.decode()) 
            print(decryted_data)
        

Running = True
password_output = generate()

while Running:
    
    with open(login, "w") as f:
        
        enter = input("Hello, please set your password for your Password Manager: ")

        m = hashlib.sha256()
        m.update(enter.encode())
        password = m.hexdigest()
        f.write(password)

        time.sleep(1)
        print("Complete!!!!")
    
        f.close()

    passcode = login.read()  
    key = gen_fernet_key(passcode)

    print("Welcome to your password manager!!! ""\n")
    
    print("Press 1 to start the process of creating a password")
    print("Press 2 to see your stored passwords")
    print("Press 3 to quit" "\n")
    
    choice = input("Choose an option:")


    if choice == "1":

        print("What is your password being used for?")

        print("Sidenote: if you dont't wish to specify leave blank")

        usage = input("Write here what its being used for:")

        General_info = {"Password: " :  password_output ,  "  Usage: "   : usage ,  " Created : " :  actual_Date ,  "  Expiry:  "  : actual_Expiry}
        
        file_writer(General_info,path)

 
    elif choice == "2":

        if os.stat(path).st_size == 0:
            print("Currently there are no saved passwords.")
        else:
            file_reader(path)


    elif choice == "3":
        Running = False
        print("Byee!!!")
    
    else:
        print("Invalid Option")


    



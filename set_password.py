import hashlib

file = "Password.txt"

with open(file,"w") as f:
    enter = input("Enter a password:")
    m = hashlib.sha256()
    m.update(enter.encode())
    password = m.hexdigest()
    f.write(password)
    f.close

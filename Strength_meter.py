from math import log2

def strength_meter(password):
    
    length = len(password)
    
    possible_symbols = 26
    possible_combos = possible_symbols**length
    bits_of_Entrophy = round(log2(possible_combos),2)
    
    if bits_of_Entrophy <=18.8:
        print("Password is Very Weak")

    elif bits_of_Entrophy > 18.8 and bits_of_Entrophy <=37.6:
        print("Password is quite Weak")

    elif bits_of_Entrophy >37.6 and bits_of_Entrophy <=56.4:
        print("Password is moderate")

    elif bits_of_Entrophy >56.4 and bits_of_Entrophy <=75.2:
        print("Password is Good")

    elif bits_of_Entrophy >75.2 and bits_of_Entrophy <=95:
        print("Password is Strong")
        
    elif bits_of_Entrophy > 95:
        print("Your Password is Very strong") 







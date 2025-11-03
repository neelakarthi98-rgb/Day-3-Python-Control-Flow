import random
import string
def generate_password(length,use_numbers,use_symbols):
    
    if length >=8:
        print("your password")
    else:
        return
        
    pool=string.ascii_letters
    if use_numbers==True:
        pool+=string.digits
    if use_symbols==True:
        pool+=string.punctuation
    if not pool:
        print("single character is must") 
    password = ''.join(random.choice(pool) for i in range(length))
    return password
pw1=generate_password(length=7,use_numbers=False,use_symbols=False)
print(f"generate password is:{pw1}") 
pw2=generate_password(length=8,use_numbers=False,use_symbols=True)                 
print(f"generate password is:{pw2}") 
pw3=generate_password(length=9,use_numbers=True,use_symbols=False)                 
print(f"generate password is:{pw3}") 
pw4=generate_password(length=9,use_numbers=False,use_symbols=False)                 
print(f"generate password is:{pw4}") 

            



     
    
  
        



    
           
    
        


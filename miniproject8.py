import random
secret_number=random.randint(1,10)

guess=0
while guess!=secret_number:
    try:
        guess=int(input("enter the number:"))
    except ValueError:
        print("your number is wrong pls try again")
        continue
    
    if guess > secret_number:
        print("your number is too high!")
    elif guess < secret_number:
        print("your number is too low")
    else:
        print("correct answer")

          


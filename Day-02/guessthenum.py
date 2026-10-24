import random
num=random.randint(1,10)
guess=int(input('Guess the number between 1 1nd 10: '))
if guess==num:
    print("You guessed it right!")
else:
    print(f"wrong! the number was {num}.")    

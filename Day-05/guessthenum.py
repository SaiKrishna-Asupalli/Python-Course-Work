import random

random=random.randint(1,10)
guess=0

while guess!=random:
    guess=int(input("Guess a num between 1 to 10:"))
    if guess>random:
        print("Too high")
    elif guess<random:
        print("Too low")
    else:
        print("Congratulations! You guessed correctly.")
  

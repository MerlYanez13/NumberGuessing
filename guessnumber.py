import random
print("This is a Number Guessing Game")
num=random.randint(1,9)
chances=0
print("Guess a number between 1-9")
while chances<5:
    guess=int(input("enter your guess :"))
    if guess==num:
        print ("You guessed correctly!")
        break
    elif guess<num:
        print ("Your guess is too low")
    else:
        print ("your guess it too high")
    chances+=1
if chances>=5:
    print("You lose")
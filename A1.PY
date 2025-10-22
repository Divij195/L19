import random
playing=True
num=str(random.randint(10,20))
print("Lets guess random number between 10 to 20")
print("The Game will end when you guess the correct answer")
while playing:
    guess=input("Enter your guess: ")
    if guess==num:
        print("You guessed it right")
        break
    else:
        print("Try again")

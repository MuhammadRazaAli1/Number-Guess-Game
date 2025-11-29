import random 
ran = random.randint(1 , 100)
print("Welcome to Number Guess Game!")
guesses = 0
number = -1
while (number != ran):
    guesses += 1
    number = int(input("Guess the Number: "))
    if number > ran:
        print(f"Enter Lower Number!")
    else:
        print(f"Enter Higher Number!")
print(f"You Guess the number \"{ran}\" in {guesses} guesses.")

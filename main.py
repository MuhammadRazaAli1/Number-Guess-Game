# Import random module to generate random number
import random 

print("Welcome to Number Guess Game!")

# Generate a random number between 1 and 100
ran = random.randint(1 , 100)

guesses = 0 # Counter for number of guesses
number = -1  # Initialize user guess

while (number != ran):
    number = int(input("Guess the Number: ")) # Take user input

    if number > ran:
        print(f"Enter Lower Number!") # Hint for user
        guesses += 1
    elif number < ran:
        print(f"Enter Higher Number!") # Hint for user
        guesses += 1
print(f"You have guess the number {ran} correclty in {guesses} attempts.") # Success message

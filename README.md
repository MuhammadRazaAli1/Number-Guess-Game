# Number Guess Game
Welcome to the Number Guess Game, an engaging logic-based challenge built entirely in Python using a simple and interactive command-line interface (CLI). This project demonstrates core Python fundamentals like random number generation, loops, conditional logic, user input handling, and iterative problem-solving through engaging gameplay.

## Project Overview
Number Guess Game is a classic guessing challenge where players compete against the computer in a thrilling race to discover a hidden number. The computer randomly selects a secret number between 1 and 100, and the player must guess it through strategic attempts. With each incorrect guess, the game provides helpful hints—directing the player to guess higher or lower. This creates an exciting, interactive experience that tests logical thinking and deduction skills while tracking the total number of attempts.

## Features
* Random number generation between 1 and 100
* Interactive guessing interface with real-time feedback
* Smart hint system (Enter Higher/Lower Number)
* Attempt counter to track player performance
* Input validation for numeric values
* Continuous gameplay until the correct number is guessed
* Clear success message displaying final result
* Beginner-friendly, clean, and readable Python code
* Encouraging feedback messages for better user experience
* Unlimited replay capability for multiple rounds

## How It Works
* The program welcomes the player and generates a random secret number between 1 and 100.
* An attempt counter is initialized to track total guesses.
* The game enters a continuous loop awaiting player input.
* The player enters their guess through the command-line interface.
* The game compares the guess with the secret number.
* If the guess is too high, a "Lower" hint is displayed, and the attempt counter increments.
* If the guess is too low, a "Higher" hint is displayed, and the attempt counter increments.
* If the guess matches the secret number, the loop terminates, and a success message is shown.
* The final message displays the correct number and total attempts taken.

## Gameplay Strategy
The game rewards strategic thinking:

* **Process of Elimination** - Use hints to narrow down the range
* **Binary Search Approach** - Start with 50, then adjust based on feedback
* **Pattern Recognition** - Track previous guesses to avoid repetition
* **Logical Deduction** - Use mathematical reasoning to optimize attempts

## Example Gameplay
```
Welcome to Number Guess Game!
Guess the Number: 50
Enter Higher Number!
Guess the Number: 75
Enter Lower Number!
Guess the Number: 62
Enter Lower Number!
Guess the Number: 56
Enter Higher Number!
Guess the Number: 59
Enter Higher Number!
Guess the Number: 61
You have guess the number 61 correctly in 6 attempts.
```

## Difficulty Levels
The game naturally adjusts difficulty based on the random number:
* **Easy** - Numbers closer to 50 (middle range)
* **Medium** - Numbers in the 30-70 range
* **Hard** - Numbers near extremes (1-20 or 80-100)

## Concepts Used
* random.randint() for generating random numbers within a specified range
* While loops for continuous gameplay until condition is met
* Conditional logic (if-elif-else) for comparing guesses with the secret number
* Counter variables for tracking attempts and game progress
* User input handling through input() and int() conversion
* String formatting with f-strings for dynamic output messages
* Variable initialization and manipulation
* Hints and feedback mechanisms for improved user experience
* User interaction through CLI (Command-Line Interface)
* Game loop implementation and flow control

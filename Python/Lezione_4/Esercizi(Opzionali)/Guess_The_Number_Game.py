# 2. Guess the Number Game:

# Create a function that generates a random number within a range specified by the user.
# Prompt the user to guess the number within a specified maximum number of attempts.
# Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
# Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.

import random

def generate_number():

    start = int(input("Insert the start of the range: "))
    end = int(input("Insert the end of the range: "))

    number = random.randint(start, end)

    print("You have 5 attempts to guess the number that has just been generated!")

    for i in range(6):
        
        if i == 5:
            print("")
            print(f"You lose! The number was {number}.")
            break
        
        print("")
        guess = int(input("Please insert your guess: "))
        
        if guess == number:
            print("")
            print(f"You win! The number was {number}")
            break
        
        elif guess < number:
            print(f"Too low! Try higher.")

        elif guess > number:
            print(f"Too high! Try lower.")

generate_number()
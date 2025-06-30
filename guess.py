print('Name:karim s mulla \nUSN: 1AY24AI052 \nSection: M\n ')

import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    guess = None
    attempts = 0

    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 10.")

    while guess != number_to_guess:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low. Try again.")
            elif guess > number_to_guess:
                print("Too high. Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

guess_the_number()

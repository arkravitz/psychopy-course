"""
Further exercises (you can do none, a few, or all of these):
Change the maximum possible number to guess.
Use a class to contain the guess data and methods.
Create a "leaderboard" and save it in the format
    "<user>, <number>, <guesses_taken>"
    You'll have to add the ability to get the user input at the beginning for
        their name
guess(int) can fail if the user doesn't enter a valid number.
    Fix this using try-except.
    If the input is invalid, let the user know and ask again.
Play around with the code and have fun!

Questions to think about:
Why did I use log_2 of the maximum number as the number of guesses allowed?
  Is there a better number for this?
  Can the user always win?
What is the correct strategy for this game?
  Hint: Google "binary search"
"""
import math
import random

MAX_NUM = 20
NUM_GUESSES = math.ceil(math.log(MAX_NUM, 2))


def generate_number():
    number = random.randint(1, MAX_NUM)
    print('I have chosen a number between 1 and {}'.format(MAX_NUM))
    return number


def allow_guess(number):
    """
    Input: Takes in the number which the user is to guess
    Gets user input and tells the user whether the number is too high
        or too low
    Returns false if the guess is wrong and True if correct
    """
    print('Guess a number')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')
        return False

    elif guess > number:
        print('Your guess is too high.')
        return False

    else:  # If guess is equal to number
        return True


if __name__ == "__main__":
    guesses_taken = 0
    number = generate_number()

    while guesses_taken < NUM_GUESSES:
        correct_guess = allow_guess(number)
        guesses_taken += 1
        if correct_guess:
            print('Great Job! You guessed the number {} in {} guesses!'.format(
                number, guesses_taken))
            break

    if not correct_guess:
        print('You ran out of guesses. The number I was thinking of was {}'.
              format(number))

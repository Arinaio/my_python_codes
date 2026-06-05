"""The program picks a random number between 1 and 100.
You keep guessing until you get it right.
After each wrong guess it tells you if you went too high or too low.
At the end it shows how many attempts it took you."""

import random

def number_game():
    num = random.randint(1, 100)
    tries = 0

    print("I picked a number between 1 and 100. Can you guess it?")

    while True:
        guess = int(input("Your guess: "))
        tries += 1

        if guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")
        else:
            print(f"You got it in {tries} tries!")
            break

number_game()

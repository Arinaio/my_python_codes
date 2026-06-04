"""A dice rolling guessing game. A dice is rolled and you have to guess the number.
- Wrong guess -> the dice is rolled again and you try again
- Right guess -> you win!
Tracks how many rolls it took you to finally guess correctly."""
import random
rolls=0
while True:
  dice=random.randint(1,6)
  rolls+=1
  guess=int(input("Guess the dice roll: "))
  if guess == dice:
    print(f"You win! The number was {dice}. you got it in {rolls} rolls.")
    break
  else:
    print(f"Wrong! The number was {dice}.rolling again...")

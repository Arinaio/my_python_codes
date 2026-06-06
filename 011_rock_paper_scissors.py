"""Rock Paper Scissors
A classis game against the computer. You choose how many round, and
first to win that many rounds wins."""

import random

options=("rock","paper","scissors")

def computer_choice():
    choice=random.choice(options)
    return choice

def user_choice():
    choice=input("rock/paper/scissors?").lower()
    while choice not in options:
        choice=input("unvalid choice. choose again (rock/paper/scissors):")
    return choice

def check_winner(user, computer):
    if user==computer:
        return "tie"
    elif user == "rock" and computer == "scissors":
        return "user"
    elif user=="scissors" and computer=="paper":
        return "user"
    elif user=="paper" and computer== "rock":
        return "user"
    else:
        return "computer"
    
def Game():
    num=int(input("how many rounds to win?"))
    user_wins=0
    computer_wins=0
    
    while user_wins<num and computer_wins<num:
        user=user_choice()
        computer=computer_choice()
        print(f"computer chose:{computer}")
        
        winner=check_winner(user,computer)
        if winner=="tie":
            print(f"It's a tie! you={user}, computer={computer}")
        elif winner=="user":
            user_wins+=1
            print(f"You win this round! you={user}, computer={computer} \n {user_wins}-{computer_wins}")
        elif winner=="computer":
            computer_wins+=1
            print(f"computer wins this round! you={user}, computer={computer} \n {user_wins}-{computer_wins}")
    if user_wins==num:
        print(f"you won the game! {user_wins}-{computer_wins}")
    else:
        print(f"computer won the game! {user_wins}-{computer_wins}")

Game()

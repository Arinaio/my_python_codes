"""Simple Story Generator
Pick or type a character and setting, and get a randomly generated silly story.
Uses functions, lists, and random."""

import random

def get_character():
    characters=["A dramatic detective", "A calm killer", "An angry father", "A lost astronaut", "A kind witch", "A lazy girl"]
    print("\nChoose a character: ")
    for i, character in enumerate(characters):
        print(f"{i+1}) {character}")
    print("7) Type my own")
    choice=input("\nYour choice (1-7): ")
    if choice=="7":
        return input("Enter your character: ")
    elif choice in ["1","2","3","4", "5", "6"]:
        return characters[int(choice)-1]
    else:
        print("Invalid choice, giving you a random one!")
        return random.choice(characters)

def get_setting():
    settings=["a haunted house", "the surface of Mars", "a school", "an empty pool", "the Stark tower", "Hogwarts"]
    print("\nChoose a setting: ")
    for i, setting in enumerate(settings):
        print(f"{i+1}) {setting}")
    print("7) Type my own")
    choice=input("\nYour choice (1-7): ")
    if choice=="7":
        return input("Enter your setting: ")
    elif choice in ["1","2","3","4", "5", "6"]:
        return settings[int(choice)-1]
    else:
        print("Invalid choice, giving you a random one!")
        return random.choice(settings)

def build_story(character, setting):
    problems=[
        "got lost",
        "lost their phone",
        "got attacked by Cyrus the Great",
        "lost their phone",
        "accidentaly started a revolution",
        "were kidnapped by Donald Trump"
        ]
    
    endings=[
        "and was never seen again.",
        "and their body was found at the White House.",
        "and honestly? they were fine with it.",
        "and posted about it online immediately",
        "and blamed it on Mervury"
        ]
    
    problem=random.choice(problems)
    ending=random.choice(endings)
    
    print(f"\n{'='*45}")
    print(f"   Once upon a time, {character} wandered into {setting}. \nThey {problem}, {ending}")
    print(f"{'='*45}")

    
def main():
    print("Welcome to the Silly Story Generator!")

    character=get_character()
    setting=get_setting()
    build_story(character, setting)

    again=input("Generate another story? (yes/no) :").lower()
    if again== "yes":
        main()

main()






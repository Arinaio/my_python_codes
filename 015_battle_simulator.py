"""Battle Simulator- Marvel vs DC
Pick two characters and see who wins!"""

import random

def get_characters():
    characters=[
        #Marvel
        {"name": "Iron Man",         "health": 95,   "attack":95,   "defense":90},
        {"name": "Thor",             "health":120,   "attack":98,   "defense":85},
        {"name": "Captain America",  "health":105,   "attack":95,   "defense":90},
        {"name": "Black Widow",      "health":80,    "attack":85,   "defense":88},
        {"name": "Spider Man",       "health":90,    "attack":90,   "defense":86},
        {"name": "Hulk",             "health":140,   "attack":98,   "defense":70},
        {"name": "Doctor Strange",   "health":90,    "attack":96,   "defense":88},
        {"name": "Black Panther",    "health":95,    "attack":87,   "defense":91},
        {"name": "Hawkeye",          "health":80,    "attack":88,   "defense":80},
        {"name": "Scarlet Witch",    "health":85,    "attack":99,   "defense":80},
        #DC
        {"name": "Batman",           "health":90,    "attack":95,   "defense":95},
        {"name": "Superman",         "health":130,   "attack":100,  "defense":95},
        {"name": "Wonder Woman",     "health":115,   "attack":95,   "defense":90},
        {"name": "The Flash",        "health":85,    "attack":92,   "defense":80},
        {"name": "Joker",            "health":80,    "attack":88,   "defense":70},
        {"name": "Aquaman",          "health":115,   "attack":88,   "defense":85},
        {"name": "Green Arrow",      "health":82,    "attack":84,   "defense":82},
        {"name": "Cyborg",           "health":100,   "attack":87,   "defense":88},
        {"name": "Shazam",           "health":110,   "attack":91,   "defense":84},
        {"name": "Harley Quinn",     "health":82,    "attack":86,   "defense":72},
        ]
    return characters

def show_characters(characters):
    print("\n---Marvel---")
    marvel=[c for c in characters if c["name"] in ["Iron Man", "Thor", "Captain America", "Black Widow", "Spider Man", "Hulk", "Doctor Strange","Black Panther", "Hawkeye", "Scarlet Witch"]]
    for i, c in enumerate(marvel):
        print(f"{i+1}) {c['name']:<20} HP:{c['health']} ATK:{c['attack']} DEF:{c['defense']}")
        
    print("\n---DC---")
    dc=[c for c in characters if c["name"] not in ["Iron Man", "Thor", "Captain America", "Black Widow", "Spider Man", "Hulk", "Doctor Strange","Black Panther", "Hawkeye", "Scarlet Witch"]]        
    for i, c in enumerate(dc):     
        print(f"{i+1+len(marvel)}) {c['name']:<20} HP:{c['health']} ATK:{c['attack']} DEF:{c['defense']}")
    
    print(f"\n{len(characters)+1}) Create my own")
    print("-"*45)
    
def pick_character(characters, player_num):
    show_characters(characters)
    choice = input(f"\nPlayer {player_num}, pick a character (1-{len(characters) + 1}): ")

    if choice == str(len(characters) + 1):
        name = input("Character name: ")
        health = int(input("Health (e.g. 100): "))
        attack = int(input("Attack (e.g. 85): "))
        defense = int(input("Defense (e.g. 70): "))
        return {"name": name, "health": health, "attack": attack, "defense": defense}
    elif choice in [str(i) for i in range(1, len(characters) + 1)]:
        return characters[int(choice) - 1].copy() #so the original list stays clean
    else:
        print("Invalid choice, picking random!")
        return random.choice(characters).copy()


def calculate_damage(attacker, defender):
    base = attacker["attack"] - (defender["defense"] // 3) #defense doesn't fully block, only 1/3 of it counts. no decimals!
    variation= random.randint(-10,10) #Makes every hit slightly different, so not all the rounds are identical and boring.
    damage = max(5, base + variation) #because if variation is very negative and the defense super high, our damage wouldn't be negative.(minimum damage is 5)
    return damage


def battle(fighter1, fighter2):
    print(f"\n{'=' * 45}")
    print(f"  ⚔️  {fighter1['name']}  VS  {fighter2['name']}  ⚔️")
    print(f"{'=' * 45}")

    round_num = 1

    while fighter1["health"] > 0 and fighter2["health"] > 0:
        print(f"\n--- Round {round_num} ---")
        #randomly decide who goes first in the round
        if random.random()>0.5:
            first, second= fighter1, fighter2
        else:
            first, second= fighter2, fighter1

        damage1 = calculate_damage(first, second)
        second["health"] -= damage1
        second["health"] = max(0, fighter2["health"]) #so health wouldn't be negative
        print(f"💥 {first['name']} hits {second['name']} for {damage1} damage! (HP: {second['health']})")

        if second["health"] <= 0:
            break

        damage2 = calculate_damage(second, first)
        first["health"] -= damage2
        first["health"] = max(0, first["health"]) 
        print(f"💥 {second['name']} hits {first['name']} for {damage2} damage! (HP: {first['health']})")

        round_num += 1

    print(f"\n{'=' * 45}")
    if fighter1["health"] > 0:
        print(f"  🏆 {fighter1['name']} WINS after {round_num} rounds!")
    else:
        print(f"  🏆 {fighter2['name']} WINS after {round_num} rounds!")
    print(f"{'=' * 45}\n")


def main():
    print("⚔️  Welcome to the Marvel vs DC Battle Simulator!")

    characters = get_characters()

    fighter1 = pick_character(characters, 1)
    fighter2 = pick_character(characters, 2)
    
    while fighter1["name"] == fighter2["name"]:
        print("❌ Can't pick the same character! Pick again.")
        fighter2 = pick_character(characters, 2)

    battle(fighter1, fighter2)

    again = input("Battle again? (yes/no): ").lower()
    if again == "yes":
        main()


main()

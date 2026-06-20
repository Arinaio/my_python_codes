"""Fishing Game
Cast your rod, catch fish based on luck and rod level, sell fish for coins,
upgrade your rod, and keep your hunger up by eating fish!
Uses functions, random, dictionaries, and error handling.
"""

import random

# Fish types: name, value (coins when sold), hunger restored when eaten
FISH_TYPES = [
    {"name": "Old Boot",        "value": 0,   "hunger": 0,   "rarity": "junk"},
    {"name": "Small Fish",      "value": 5,   "hunger": 10,  "rarity": "common"},
    {"name": "Tuna",            "value": 15,  "hunger": 25,  "rarity": "common"},
    {"name": "Salmon",          "value": 30,  "hunger": 35,  "rarity": "uncommon"},
    {"name": "Golden Fish",     "value": 80,  "hunger": 50,  "rarity": "rare"},
    {"name": "Legendary Shark", "value": 200, "hunger": 100, "rarity": "legendary"},
]

# Each rod level has different chances per rarity (must add up to 100)
ROD_LEVELS = {
    1: {"junk": 30, "common": 55, "uncommon": 12, "rare": 3,  "legendary": 0},
    2: {"junk": 20, "common": 50, "uncommon": 20, "rare": 8,  "legendary": 2},
    3: {"junk": 10, "common": 40, "uncommon": 28, "rare": 17, "legendary": 5},
}

UPGRADE_COST = {2: 50, 3: 150}


def cast_rod(rod_level):
    chances = ROD_LEVELS[rod_level]

    # build a weighted pool based on chances
    pool = []
    for rarity, chance in chances.items():
        pool.extend([rarity] * chance)

    caught_rarity = random.choice(pool)
    possible_fish = [f for f in FISH_TYPES if f["rarity"] == caught_rarity]
    fish = random.choice(possible_fish)
    return fish


def eat_fish(fish, hunger):
    hunger += fish["hunger"]
    hunger = min(100, hunger)
    return hunger


def sell_fish(fish, coins):
    coins += fish["value"]
    return coins


def show_status(coins, hunger, rod_level):
    print(f"\n💰 Coins: {coins} | 🍖 Hunger: {hunger}/100 | 🎣 Rod Level: {rod_level}")


def show_inventory(inventory, mode):
    print("\n--- Your fish ---")
    for i, fish in enumerate(inventory):
        if mode == "eat":
            print(f"{i + 1}) {fish['name']} - hunger: {fish['hunger']}")
        elif mode == "sell":
            print(f"{i + 1}) {fish['name']} - value: {fish['value']}")


def upgrade_rod(rod_level, coins):
    if rod_level >= 3:
        print("Your rod is already at max level!")
        return rod_level, coins

    cost = UPGRADE_COST[rod_level + 1]

    try:
        if coins < cost:
            raise ValueError(f"Not enough coins! Need {cost}, you have {coins}.")

        coins -= cost
        rod_level += 1
        print(f"🎉 Rod upgraded to level {rod_level}!")

    except ValueError as e:
        print(f"❌ {e}")

    return rod_level, coins


def main():
    print("🎣 Welcome to the Fishing Game!")

    coins = 0
    hunger = 70
    rod_level = 1
    inventory = []

    while True:
        show_status(coins, hunger, rod_level)

        if hunger <= 0:
            print("\n💀 You starved! Game over.")
            break

        print("\nWhat do you want to do?")
        print("1) Cast your rod (costs 5 hunger)")
        print("2) View inventory")
        print("3) Eat a fish")
        print("4) Sell a fish")
        print("5) Upgrade rod")
        print("6) Quit")

        choice = input("\nYour choice: ")

        if choice == "1":
            if hunger < 5:
                print("Too hungry to fish! Eat something first.")
                continue

            hunger -= 5
            fish = cast_rod(rod_level)
            inventory.append(fish)
            print(f"🎣 You caught: {fish['name']} ({fish['rarity']})!")

        elif choice == "2":
            if not inventory:
                print("Your inventory is empty!")
            else:
                print("\n--- Inventory ---")
                for i, fish in enumerate(inventory):
                    print(f"{i + 1}) {fish['name']} - value: {fish['value']}, hunger: {fish['hunger']}")

        elif choice == "3":
            if not inventory:
                print("No fish to eat!")
                continue

            show_inventory(inventory, "eat")

            try:
                index = int(input("Which fish number to eat? ")) - 1
                fish = inventory.pop(index)
                hunger = eat_fish(fish, hunger)
                print(f"😋 You ate {fish['name']}! Hunger: {hunger}/100")
            except (ValueError, IndexError):
                print("❌ Invalid fish number!")

        elif choice == "4":
            if not inventory:
                print("No fish to sell!")
                continue

            show_inventory(inventory, "sell")

            try:
                index = int(input("Which fish number to sell? ")) - 1
                fish = inventory.pop(index)
                coins = sell_fish(fish, coins)
                print(f"💰 Sold {fish['name']} for {fish['value']} coins!")
            except (ValueError, IndexError):
                print("❌ Invalid fish number!")

        elif choice == "5":
            rod_level, coins = upgrade_rod(rod_level, coins)

        elif choice == "6":
            print("Goodbye! 🎣")
            break

        else:
            print("Invalid choice, try again!")


main()

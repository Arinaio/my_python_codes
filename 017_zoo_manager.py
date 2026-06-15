"""Tehran Zoo Manager
Add animals to your zoo, view their info, and make them speak!
Uses classes, inheritance. Built while learning OOP in Python"""


class Animal:
    zoo_name = "Tehran Zoo"

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def info(self):
        print(f"""
--- Animal Info ---
Name:    {self.name}
Species: {self.species}
Age:     {self.age}
Zoo:     {self.zoo_name}
        """)

    def __str__(self):
        return f"{self.name} ({self.species}, {self.age} years old)"


class Bird(Animal):
    def __init__(self, name, age, sound, wing_span):
        super().__init__(name, "Bird", age, sound)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} tweets: {self.sound}!")

    def info(self):
        super().info()
        print(f"Wing Span: {self.wing_span}cm")


def create_animal():
    print("\nWhat type of animal? (1) Regular  (2) Bird")
    choice = input("Choice: ").strip()

    name = input("Name: ").strip()
    age = int(input("Age: "))
    sound = input("Sound it makes: ").strip()

    if choice == "2":
        wing_span = int(input("Wing span (cm): "))
        return Bird(name, age, sound, wing_span)
    else:
        species = input("Species: ").strip()
        return Animal(name, species, age, sound)


def main():
    animals = []

    while True:
        print("\n=== Tehran Zoo ===")
        print("1. Add animal")
        print("2. List all animals")
        print("3. Make an animal speak")
        print("4. Exit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            animal = create_animal()
            animals.append(animal)
            print(f"\nAdded: {animal}")

        elif choice == "2":
            if not animals:
                print("No animals yet.")
            for i, animal in enumerate(animals, 1):
                print(f"{i}. {animal}")
                animal.info()

        elif choice == "3":
            if not animals:
                print("No animals yet.")
            else:
                for i, animal in enumerate(animals, 1):
                    print(f"{i}. {animal.name}")
                index = int(input("Pick number: ")) - 1
                if 0 <= index < len(animals):
                    animals[index].make_sound()

        elif choice == "4":
            print("Goodbye!")
            break


main()

"""Pet Class
Create pets, feed them, play with them, and check their mood.
my first OOP project!"""

class pet():
    def __init__(self, name, animal_type):
        self.name=name
        self.animal_type=animal_type
        self.hunger = 50
        self.happiness = 50
        
    def eat(self):
        if self.hunger == 0:
            print(f"{self.name} is not hungry!")
        else:
            self.hunger -= 20
            self.hunger = max(0,self.hunger)
            print(f"{self.name} eats happily!😋 (hunger:{self.hunger})")
            
    def play(self):
        if self.happiness == 100:
            print(f"{self.name} is too tired to play.")
        else:
            self.happiness += 20
            self.happiness = min(100, self.happiness)
            self.hunger += 10
            self.hunger = min(100, self.hunger)
            print(f"{self.name} plays!⚾ (Happiness: {self.happiness})")
            
    def speak(self):
        if self.animal_type== "cat":
            print(f"{self.name} says meow!🐈")
        elif self.animal_type== "dog":
            print(f"{self.name} says woof!🐕")
        elif self.animal_type== "bird":
            print(f"{self.name} says tweet!🐦")
            
    def mood(self):
        print(f"--- {self.name}'s status ---")
        print(f"Type:        {self.animal_type}")
        print(f"Hunger:      {self.hunger}/100")
        print(f"Happiness:   {self.happiness}/100")
        
        if self.hunger >= 80:
            print("Mood: Starving! 😢 Feed me!")
        elif self.happiness >= 80:
            print("Mood: Super happy!😁")
        elif self.happiness <= 30:
            print("Mood: Sad... Play with me😔")
        else:
            print("Mood: Doing okay 😊")
    
    def rest(self):
        self.happiness -= 15
        self.happiness = max(0,self.happiness)
        self.hunger += 10
        self.hunger = min(100, self.hunger)
        print(f"{self.name} takes a nap...💤 (Happiness:{self.happiness}, Hunger:{self.hunger})")
            
            
def main():
    print("Welcome to the Pet Simulator!")
    print("What type of pet? (cat/dog/bird)")
    animal_type=input("Type:").lower()
    name=input("Pet's name:")
    
    animal= pet(name, animal_type)
    while True:
        print("\nWhat do you want to do?")
        print("1) Feed")
        print("2) Play")
        print("3) Listen to them speak")
        print("4) Check mood")
        print("5) Let them rest")
        print("6) Exit")
        
        choice=int(input("\nYour choice:"))
        
        if choice == 1:
            animal.eat()
        elif choice == 2:
            animal.play()
        elif choice == 3:
            animal.speak()
        elif choice == 4:
            animal.mood()
        elif choice == 5:
            animal.rest()
        elif choice == 6:
            print(f"Goodbye! Take care of {animal.name}!")
            break
        else:
            print("Invalid choice")
            
main()
        



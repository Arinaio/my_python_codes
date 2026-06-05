"""Generates a random strong password based onn the length you choose.
The password always contains at least one uppercase letter, one number and one symbol."""

import random

def password_generator(length=12):
    lowercase="abcdefghijklmnopqrstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols="~!@#$%^&*()_+{}[]?/><,.\=-"
    numbers="1234567890"
    all_together=lowercase+uppercase+symbols+numbers
    
    password=[random.choice(lowercase),
                random.choice(uppercase),
                random.choice(symbols),
                random.choice(numbers)]
    for i in range(length-4):
      password.append(random.choice(all_together))
    random.shuffle(password)  #shuffle mixes it
    return ''.join(password)  #turns the list into a string
length=int(input("How long should your password be?(minimum 4):"))
if length<4:
    print("Password should at least have 4 characters")
else:
    print(f"Your password:{password_generator(length)}")

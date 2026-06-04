"""A classic encryption method where every letter is shifted by a number you choose.
Example with shift 3: a-->d, b-->e, hello-->khoor
The program can both encode and decode messages."""

alphabet="abcdefghijklmnopqrstuvwxyz"
message=input("Enter your message: ").lower()
shift=int(input("Enter shift number: "))
mode=input("Encode/Decode?")
if mode=="Decode":
    shift=-shift
result=""
for i, letter in enumerate(message):
    if letter in alphabet:
        position=alphabet.index(letter)
        new_position=(position+shift)%26
        result+= alphabet[new_position]
    else:
        result+= letter
print(f"result:\n{result}")

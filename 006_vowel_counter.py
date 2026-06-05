"""The user types a sentence and the program counts how manny times each vowel(a, e, o, i, u) appears in it."""
sentence=input("Enter a sentence: ").lower()
vowels={"a":0, "e":0, "i":0, "o":0, "u":0}
for letter in sentence:
  if letter in vowels:
    vowels[letter]+=1
print("\nVowel counts:")
for vowel, count in vowels.items():
  print(f"{vowel}:{count}", end="\t")

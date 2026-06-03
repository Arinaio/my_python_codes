"""FizzBuzz
A classic counting game in which players count up from 1:
-say "Fizz" instead of any multiple of the first number
-say "Buzz" instead of any multiple of the second number
-say "FizzBuzz" for multiples of both
-Otherwise just say the number
This version lets you pick your own Fizz and Buzz numbers."""
fizz=int(input("Enter the Fizz number:"))
buzz=int(input("Enter the Buzz number:"))
limit=int(input("count up to:"))
for i in range(1,limit+1):
  if i%fizz==0 and i%buzz==0:
    print("FizzBuzz")
    continue  #it's not necessary in the program, but skips the checks below for efficiency
  elif i%fizz==0:
    print("Fizz")
    continue
  elif i%buzz==0:
    print("Buzz")
    continue
  else:
    print(i)

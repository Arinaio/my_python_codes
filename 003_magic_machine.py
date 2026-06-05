"""
This program takes a positive integer n and repeatedly applies the following rule until it reaches 1:
- If the number is even -> divide it by 2
- If the number is odd -> multiply number by 3 and add 1
"""
n=int(input("enter a number"))
while n!=1:
  print(n)
  if n%2==0:
    n=n//2
  else:
    n=3*n+1
print(n)
  

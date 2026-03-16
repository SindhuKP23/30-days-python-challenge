#Program to find strong numbers

import math

num = int(input("Enter a number:"))
temp=num
add=0
while num>0:
    digit = num%10
    add = add+(math.factorial(digit))
    num//=10
if add==temp:
   print(f"{temp} is a strong number")
else:
   print(f"{temp} is not a strong number")
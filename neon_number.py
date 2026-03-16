#Program to find Neon number

num = int(input("Enter a number:"))
temp=num
add=0 
product= num*num
while product>0:
    digit = product%10
    add = add+digit
    product//=10
if add==temp:
   print(f"{temp} is a Neon number")
else:
   print(f"{temp} is not Neon number")
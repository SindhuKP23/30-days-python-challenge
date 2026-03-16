#Program to find Harshad number

num = int(input("Enter a number:"))
temp=num
add=0
while num>0:
    digit = num%10
    add = add+digit
    num//=10
if temp%add==0:
   print(f"{temp} is a Harshad number")
else:
   print(f"{temp} is not Harshad number")
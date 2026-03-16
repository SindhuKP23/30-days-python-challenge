#Program to find strong numbers
import math

num = int(input("Enter a number:"))
strong_num=0
temp=num
sum=0
while num>0:
    digit = num%10
    strong_num=math.factorial(strong_num)+digit
    num//=10
    sum=sum+strong_num
if sum==temp:
    print(f"{sum} is strong number")
else:
    print(f"{sum} is not a  strong number")

#Program to find Armstrong number

num = int(input("Enter a number:"))
str_num=str(num)
add=0
temp=num
size=len(str_num)
while num>0:
    digit = num%10
    add=add+(digit**size)
    num//=10
if add==temp:
    print(f"{temp} is armstrong")
else:
    print(f"{temp} is not armstrong")

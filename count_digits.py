#Program to count the number of digits

num = int(input("Enter a number:"))
count=0
while num>0:
    digit = num%10
    count+=1
    num//=10
print(f"The total count of is",count)
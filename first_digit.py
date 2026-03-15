#Program to find the first digit of a number

num = int(input("Enter a number:"))
first_digit=0
temp=num
while num>0:
    digit = num%10
    first_digit=digit
    num//=10
print(f"{first_digit} is the first digit of {temp}")

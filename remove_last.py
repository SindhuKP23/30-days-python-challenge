#Program to remove the last digit of a number

num = int(input("Enter a number:"))
last_digit=0
temp=num
digit = num//10
last_digit=digit
print(f" {temp} after removing the last digit is:{last_digit}")

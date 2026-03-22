#Program to count binary

num = int(input("Enter number: "))

count = 0

while num > 0:
    if num % 2 == 1:
        count = count + 1
    num = num // 2

print("Number of 1s:", count)
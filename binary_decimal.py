#Program to convert from binary to decimal

num = int(input("Enter binary number: "))

decimal = 0
power = 0

while num > 0:
    digit = num % 10          # last digit (0 or 1)
    decimal = decimal + digit * (2 ** power)
    power = power + 1
    num = num // 10           # remove last digit

print("Decimal:", decimal)
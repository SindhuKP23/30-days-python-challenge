#Program to find LCM

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Store original values
x = a
y = b

# Find GCD
while b != 0:
    remainder = a % b
    a = b
    b = remainder

gcd = a

# Find LCM
lcm = (x * y) // gcd

print("LCM is:", lcm)
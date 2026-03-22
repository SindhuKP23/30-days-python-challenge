#Program to find binary palindrome

num = int(input("Enter number: "))

binary = 0
place = 1

# Convert to binary (as number)
temp = num
while temp > 0:
    remainder = temp % 2
    binary = binary + remainder * place
    place = place * 10
    temp = temp // 2

# Reverse number
rev = 0
temp = binary

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

# Check
if binary == rev:
    print("Binary palindrome")
else:
    print("Not binary palindrome")
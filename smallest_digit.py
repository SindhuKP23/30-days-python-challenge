#Program to smallest number of digits

num = int(input("Enter a number:"))
smallest = 9
while num>0:
    digit = num%10
    if digit<smallest:
        smallest=digit
    num//=10
print(f"The largest number is:",smallest)
#Program to product of digits

num = int(input("Enter a number:"))
product = 1
while num>0:
    digit = num%10
    product=product*digit
    num//=10
print(f"The product is :",product)
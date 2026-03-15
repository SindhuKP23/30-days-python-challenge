#Program to check palindrome

num = int(input("Enter a number:"))
palindrome=0
temp=num
while num>0:
    digit = num%10
    palindrome=palindrome*10+digit
    num//=10
if palindrome==temp:
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not palindrome")

#Program to find prime numbers.

num = int(input("Enter a number:"))
if num<=1:
    print(num,"Not Prime")
elif num==2:
    print(num,"Prime Number")
elif num%2==0:
    print(num,"Not Prime ")
else: 
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            print(num,"is Not Prime")
            break
    else:
        print(num," is Prime")
    
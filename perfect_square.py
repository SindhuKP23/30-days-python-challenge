#Program to find perfect square of a number

num=int(input("Enter a number:"))
if num<0:
    print(num,"is not a factor")
else:
    root=int(num**0.5)
    if root*root==num:
        print(num,"is a perfect square")
    else:
        print(num,"is not a perfect square")
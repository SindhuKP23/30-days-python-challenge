#Program to find the factor of a number

num=int(input("Enter a number:"))

for i in range(1,num+1):
  if num%i==0:
   print(i,"is the factors of a number")
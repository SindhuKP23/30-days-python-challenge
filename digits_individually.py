#Program to print digits individually

num = int(input("Enter a number:"))
str_num=str(num)
for i in str_num:
    print(i)
#OR 
# print(*str_num, sep=" " )
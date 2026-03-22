#Program to find power calculation

a = int(input("Enter base: "))
b = int(input("Enter power: "))

result = 1

for i in range(b):
    result = result * a

print("Answer:", result)
"""number = int(input())
print("*" * number)
for i in range(number - 2):
    print("*" + " " * (number - 2) + "*")
print("*" * number)"""


number = int(input())
print("*" * number)

for i in range(number - 2):
    print("*", end="")
    for j in range(number - 2):
        print(" ", end="")
    print("*")
print("*" * number)

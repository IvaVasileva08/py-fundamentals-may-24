"""number = int(input())
for i in range(number, 0, -1):
    for j in range(i):
        print("*", end="")
    print()"""

number = int(input())
for i in range(number, 0, -1):
    print("*" * i)
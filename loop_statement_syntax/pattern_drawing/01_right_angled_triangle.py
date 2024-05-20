"""number = int(input())
for i in range(1, number + 1):
    for j in range(0, i):
        print("*", end="")
    print()"""


number = int(input())
for i in range(1, number + 1):
    print("*" * i)
number = int(input())

# Горна част на ромба
for row in range(1, number + 1, 2):
    spaces = (number - row) // 2
    print(" " * spaces + "*" * row)

# Долна част на ромба
for row in range(number - 2, 0, -2):
    spaces = (number - row) // 2
    print(" " * spaces + "*" * row)
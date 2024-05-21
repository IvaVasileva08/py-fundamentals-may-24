"""number = input()
sorted_number = sorted (number)
revers_number = reversed (sorted_number)
new_number = ''.join(revers_number)
print(new_number)
"""


number = input()
n = len(number)
for i in range(n):
    for j in range(0, n - i - 1):
        if number[j] < number[j + 1]:
            number = number[:j] + number[j + 1] + number[j] + number[j + 2:]
print(number)

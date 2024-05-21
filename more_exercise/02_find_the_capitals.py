"""text = input()
array = []
for i in range(len(text)):
    if 'A' <= text[i] <= 'Z' or 'А' <= text[i] <= 'Я':
        array.append(i)
print(array)"""


text = input()
array = []
for i in range(len(text)):
    if text[i].isupper():
        array.append(i)
print(array)

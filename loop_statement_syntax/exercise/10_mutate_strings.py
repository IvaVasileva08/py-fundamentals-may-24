first_string = input()
second_string = input()
last_string = first_string

for index in range(len(first_string)):
    left_part = second_string[:index + 1]
    right_part = first_string[index + 1:]
    new_string = left_part + right_part
    if new_string != last_string:
        print(new_string)
        last_string = new_string
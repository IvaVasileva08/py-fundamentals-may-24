command = input()
counter= 0
while command != "END":
    if command.lower() == "coding" or \
            command.lower() == "dog" or \
            command.lower() == "cat" or \
            command.lower() == "movie":
        if command.islower():
            counter += 1
        else: counter += 2
    command = input()
if counter > 5: print("You need extra sleep")
else: print(counter)
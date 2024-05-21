animals_input = input()
animals = []
current_animal = ""

for char in animals_input:
    if char == ",":
        animals.append(current_animal)
        current_animal = ""
    elif char.isalpha():
        current_animal += char
animals.append(current_animal)
wolf_index = animals.index("wolf")
if wolf_index == len(animals) - 1:
    print("Please go away and stop eating my sheep")
else:
    sheep_number = len(animals) - wolf_index - 1
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
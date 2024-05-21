my_string = input().lower()
keywords = ["sand", "water", "fish", "sun"]
total_count = 0
for word in keywords:
    word_count = 0
    for i in range(len(my_string)):
        if my_string[i:i+len(word)] == word:
            word_count += 1
    total_count += word_count
print(total_count)

"""my_string = input().lower()
calculate = 0
sand_count = my_string.count("sand")
water_count = my_string.count("water")
fish_count = my_string.count("fish")
sun_count = my_string.count("sun")
calculate = sun_count + fish_count + water_count + sand_count
print(calculate)"""
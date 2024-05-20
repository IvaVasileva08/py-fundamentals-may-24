budget = float(input())
flour_price = float(input())
count_bread = 0
color_egg = 0

egg_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
bread_price = flour_price + egg_price + milk_price

while budget >= bread_price:
    budget -= bread_price
    count_bread += 1
    color_egg += 3

    if count_bread % 3 == 0:
        lost_eggs = count_bread - 2
        color_egg -= lost_eggs
money_left = budget
print(f"You made {count_bread} loaves of Easter bread! Now you have {color_egg} eggs and {money_left:.2f}BGN left.")
number_of_orders = int(input())
sum = 0.00

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    coffee = price_per_capsule * days * capsules_per_day
    sum+=coffee
    print(f"The price for the coffee is: ${coffee:.2f}")
print(f"Total: ${sum:.2f}")
budget = int(input())
product = input()
while product != "End":
    price = int(product)
    budget -= price
    if budget < 0:
        print("You went in overdraft!")
        break
    product = input()
else:
    print("You bought everything needed.")
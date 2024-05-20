number = int(input())

for numeric in range(number):
    message = int(input())
    if message == 88:
        print("Hello")
    if message == 86:
        print("How are you?")
    if message != 86 and message!= 88 and message < 88:
        print("GREAT!")
    if message > 88:
        print("Bye.")
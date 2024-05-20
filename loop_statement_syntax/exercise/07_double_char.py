mystring = input()
while mystring != "End":
    if mystring != "SoftUni":
        newstring = ""
        for letter in mystring:
            newstring += letter * 2
        print(newstring)
    mystring = input()
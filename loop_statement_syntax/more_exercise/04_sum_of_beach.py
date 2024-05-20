mystring = input().lower()
calculate = 0
str1 = "Sand".lower()
str2 = "Water".lower()
str3 = "Fish".lower()
str4 = "Sun".lower()
if str1 in mystring: calculate += 1
if str2 in mystring: calculate += 1
if str3 in mystring: calculate += 1
if str4 in mystring: calculate += 1
print(calculate)
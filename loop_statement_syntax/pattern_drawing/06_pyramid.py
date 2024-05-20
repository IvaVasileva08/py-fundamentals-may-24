"""number = int(input())
for row in range(1, number + 1):
    spaces = number - row
    print(" " * spaces, end="")
    print("*" * (2 * row - 1))"""
"""6 *
    ***
   *****
  *******
 *********
***********"""


"""number = int(input())
for row in range(1, number + 1):
    for col in range(1, number - row + 1):
        print(" ", end="")
    for col in range(2 * row - 1):
        print("*", end="")
    print()"""
"""6 *
    ***
   *****
  *******
 *********
***********"""


"""number = int(input())
for row in range(1, number + 1):
    spaces = number - row
    stars = 2 * row - 1
    print(" " * spaces + "*" * stars)"""
"""6 *
    ***
   *****
  *******
 *********
***********"""


"""number = int(input())
for row in range(1, number + 1):
    for col in range(1, number - row + 1):
        print(" ", end="")
    print("*", end="")
    for col in range(1, row):
        print(" *", end="")
    print()"""
"""6 *
    * *
   * * *
  * * * *
 * * * * *
* * * * * *"""
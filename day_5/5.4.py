for x in range(1,101):
    stment = ""
    if x % 3 == 0:
        stment += "Fizz"
    if x % 5 == 0:
        stment += "Buzz"
    if not x % 3 == 0 and not x % 5 == 0:
        stment += str(x)
    print(stment)
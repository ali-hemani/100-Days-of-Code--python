# Write your code below this line 👇
def prime_checker(number):
    amount_divided = 0
    for i in range(1, number+1):
        if number % i == 0:
            amount_divided += 1
    if amount_divided == 2:
        print("It's a prime number")
    else:
        print("It's not a prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
total_true = 0
total_love = 0

name1_lower = name1.lower()

name2_lower = name2.lower()

total_true += name1_lower.count("t")
total_true += name1_lower.count("r")
total_true += name1_lower.count("u")
total_true += name1_lower.count("e")
total_true += name2_lower.count("t")
total_true += name2_lower.count("r")
total_true += name2_lower.count("u")
total_true += name2_lower.count("e")

total_love += name1_lower.count("l")
total_love += name1_lower.count("o")
total_love += name1_lower.count("v")
total_love += name1_lower.count("e")
total_love += name2_lower.count("l")
total_love += name2_lower.count("o")
total_love += name2_lower.count("v")
total_love += name2_lower.count("e")

love_score = int(f"{total_true}{total_love}")

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
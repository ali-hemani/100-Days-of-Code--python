# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
position_row = int(position[0]) - 1
position_column = int(position[1]) - 1
map[position_column][position_row] = "x"
print(f"{row1}\n{row2}\n{row3}")

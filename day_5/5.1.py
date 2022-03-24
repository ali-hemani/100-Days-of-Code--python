# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for num in range(0, len(student_heights)):
    student_heights[num] = int(student_heights[num])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
total = 0
for x in student_heights:
    total += x
print(int(round(total/len(student_heights), 0)))
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_ppl = input("How many people to split the bill? ")

total_tip = (100+float(tip))/100
each_person = round((float(total_bill) * total_tip)/int(num_ppl), 2)
per_person_str = "{:.2f}".format(each_person)
print(f"Each person should pay: ${per_person_str}")

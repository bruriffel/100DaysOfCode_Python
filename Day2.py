print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

percentage = tip/100 + 1
pay = (total * percentage)/people
final_pay = "{:.2f}".format(pay)

print(f"Each person should pay: ${final_pay}")

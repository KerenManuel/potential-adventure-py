print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

amount_pay = (bill / people) * (1 + tip/ 100)
total_amount = round(amount_pay, 2)

print(f"Everyone should pay: ${total_amount}")


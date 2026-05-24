print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

price = bill * (tip / 100)
total = bill + price
per_person = bill / people
cost = round(per_person, 2)

print("Each person should pay $" + str(cost))


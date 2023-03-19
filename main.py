# This is day 2 of 100 in the Python Bootcamp

#get the total bill
bill = float(input("What was the total of the bill? $"))

#set tip amount
tip = int(input("Would you like to give 12%, 15%, or 18%? "))
tip_as_percent = tip / 100
total_tip_amt = bill * tip_as_percent
#print(total_tip_amt)

bill_total = bill + total_tip_amt
#print(bill_total)

#set the number of people splitting the bill
seats = int(input("How many people are splitting the bill? "))
per_person = bill_total / seats
#print(per_person)

#round amount to 2 digits
split_amount = round(per_person, 2)

print(f"Each person should pay: ${split_amount}")
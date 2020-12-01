#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.
print("Welcome to the Tip Calculator.\n")

total_bill = float(input("What is the total bill? "))

num_people = float(input("Please enter the number of people: "))

percent_tip = float(input("How much would you like to tip? 10, 15, or 20 percent? "))

total_tip = total_bill * (percent_tip / 100)

bill_with_tip = total_bill + total_tip

split_bill = round(bill_with_tip / num_people, 2)

print(f"\nEach person owes {split_bill}.")

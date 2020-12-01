print("Welcome to the Tip Calculator.\n")

total_bill = float(input("What is the total bill? "))

num_people = float(input("Please enter the number of people: "))

percent_tip = float(input("How much would you like to tip? 10, 15, or 20 percent? "))

total_tip = total_bill * (percent_tip / 100)

bill_with_tip = total_bill + total_tip

split_bill = round(bill_with_tip / num_people, 2)

print(f"\nEach person owes {split_bill}.")

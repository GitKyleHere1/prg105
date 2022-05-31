# A program to be used to calculate the cost of tickets depending on the buying type and the number
# of tickets bought after applying a discount if applicable

# Create dictionary for pricing table
pricing_table = {
	1: ("Student", "$5.00", 5),
	2: ("Veteran", "$7.00", 7),
	3: ("Show Sponsor", "$2.00", 2),
	4: ("Retiree", "$6.00", 6),
	5: ("General Public", "$10.00", 10)
}

# Display the pricing table and ask the buyer what category they fit in to get their price per ticket
print("Pricing table:\n")

for key, price_table in pricing_table.items():
	print(str(key) + ":", price_table[0], price_table[1])

# Add spacing
print("\n")

# Ask user to enter the category they fit in, loop until we get a valid entry
while True:
	try:
		ticket_buyer = int(input("Please enter the category you fit in from the table above. "))
		if ticket_buyer in pricing_table:
			break
		else:
			print("That is not a valid choice")
	except ValueError:
		print("That is not a valid choice.")

# Ask user how many tickets they are purchasing
while True:
	try:
		num_tickets = int(input("Please enter how many tickets you would like to purchase. "))
		break
	except ValueError:
		print("That is not a valid choice.")

# Get the base ticket price
base_ticket_price = pricing_table[ticket_buyer][2]

# Calculate total cost before discounts
cost = float(num_tickets * base_ticket_price)

# Initialize discount_percent and get the discount percentage
# 4-8 = 10%
# 9-15 = 15%
# 16+ = 20%
discount_percent = 0
if num_tickets > 15:
	discount_percent = .2
elif num_tickets > 8:
	discount_percent = .15
elif num_tickets > 3:
	discount_percent = .1
else:
	discount_percent = 0

# Calculate the total discount
discount_value = float(cost * discount_percent)

# Calculate cost after discount
cost_after_discount = float(cost - discount_value)

# Calculate price per ticket after discount
discounted_ticket_price = float(base_ticket_price * (1 - discount_percent))

# Output:
# Total cost before discount added
# Discount total
# Cost after discount
# Price per ticket after discount
print("Your total cost before discounts is $%.2f." % cost)
print("Your total discount is $%.2f." % discount_value)
print("Your total cost after discounts is $%.2f." % cost_after_discount)
print("Your final price is $%.2f per ticket." % discounted_ticket_price)

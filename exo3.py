# Discount Calculation

def discount_calculation():
    try:
        # Get inputs from the user
        total_amount = float(input("Total amount: "))
        number_of_items = int(input("Number of items: "))
        day_of_week = input("Day of the week: ").strip().lower()

        # Validate inputs
        if total_amount < 0 or number_of_items < 0:
            print("Total amount and number of items must be non-negative.")
            return

        # Determine the base discount based on the day of the week
        if day_of_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
            discount = 0.10  # 10% discount
        elif day_of_week in ["saturday", "sunday"]:
            discount = 0.20  # 20% discount
        else:
            print("Invalid day of the week. Please enter a valid day.")
            return

        # Apply an additional discount if there are more than 5 items
        if number_of_items > 5:
            discount += 0.05  # Additional 5% discount

        # Calculate the total price after discount
        discounted_price = total_amount * (1 - discount)

        print(f"Total price after discount: {discounted_price:.2f} dinars")
    except ValueError:
        print("Please enter valid numeric inputs for the total amount and number of items.")

# Run the program
discount_calculation()

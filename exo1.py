# Ticket Purchase System

def ticket_purchase_system():
    # Get the user's name
    name = input("Please enter your name: ").strip()

    # Check if the user is a VIP
    if name.lower() == "vip":
        print("Enjoy the show for free!")
    else:
        try:
            # Ask for the number of tickets
            num_tickets = int(input("How many tickets would you like to buy? "))

            # Validate the input
            if num_tickets < 0:
                print("Number of tickets cannot be negative.")
                return

            # Calculate the total cost
            ticket_price = 15.50
            total_cost = num_tickets * ticket_price

            print(f"The total cost is {total_cost:.2f}")
            print("Enjoy your tickets!")
        except ValueError:
            print("Please enter a valid number of tickets.")

# Run the program
ticket_purchase_system()

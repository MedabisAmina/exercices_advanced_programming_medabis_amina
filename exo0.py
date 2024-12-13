# Taxi Ride Calculator

def calculate_taxi_rides():
    # Get input from the user
    try:
        total_people = int(input("How many people need a ride? "))
        people_per_taxi = int(input("How many people fit in one taxi? "))

        # Validate input
        if total_people <= 0 or people_per_taxi <= 0:
            print("Both numbers must be greater than 0.")
            return

        # Calculate the number of taxis required
        full_taxis = total_people // people_per_taxi
        remaining_people = total_people % people_per_taxi

        # If there's a remainder, an extra taxi is needed
        total_taxis = full_taxis + (1 if remaining_people > 0 else 0)

        print(f"Number of taxis needed: {total_taxis}")
    except ValueError:
        print("Please enter valid integers.")

# Run the program
calculate_taxi_rides()

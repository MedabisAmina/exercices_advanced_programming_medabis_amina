# Function to check if input is a valid positive integer
def get_positive_integer():
    while True:
        try:
            # Ask the user for input
            N = int(input("Please enter a positive integer: "))
            # Check if the number is positive
            if N > 0:
                return N
            else:
                print("The number must be positive. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Get a valid positive integer N
N = get_positive_integer()

# Print numbers from -N to N, excluding 0
for i in range(-N, N+1):
    if i != 0:
        print(i)

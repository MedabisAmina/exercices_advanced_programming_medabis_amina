# Print a Line of Hash Characters

def print_hash_line():
    # Request the width of the hash line from the user
    try:
        width = int(input("Width: "))

        # Validate input
        if width < 0:
            print("Width cannot be negative.")
            return

        # Print the line of hash characters
        print("#" * width)
    except ValueError:
        print("Please enter a valid integer.")

# Run the program
print_hash_line()

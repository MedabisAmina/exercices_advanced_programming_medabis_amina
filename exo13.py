# Underlined Strings Printer

def print_underlined_strings():
    while True:
        # Ask the user for a string
        user_input = input("Please type in a string: ").strip()

        # End the loop if the input is empty
        if user_input == "":
            break

        # Print the string followed by an underline
        print(user_input)
        print("-" * len(user_input))

# Run the program
print_underlined_strings()

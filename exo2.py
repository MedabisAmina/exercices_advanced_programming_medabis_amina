# Temperature Check

def temperature_check():
    try:
        # Ask the user for the temperature
        temperature = int(input("Please type in the temperature: "))

        # Check and print warnings/messages
        if temperature < 0:
            print("It's freezing!")
        if temperature < 10:
            print("It's cold!")
        if temperature < 20:
            print("It's cool!")

        # Final message
        print("Stay safe!")
    except ValueError:
        print("Please enter a valid integer for the temperature.")

# Run the program
temperature_check()

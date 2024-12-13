# Separating Dinars and Centimes

def separate_dinars_and_centimes():
    try:
        # Ask the user for the price in dinars
        price = float(input("Please type in a price: "))

        # Separate the dinars (integer part) and centimes (decimal part)
        dinars = int(price)
        centimes = int(round((price - dinars) * 100))

        # Print the results
        print(f"Dinars: {dinars}")
        print(f"Centimes: {centimes}")
    except ValueError:
        print("Please enter a valid positive floating-point number.")

# Run the program
separate_dinars_and_centimes()

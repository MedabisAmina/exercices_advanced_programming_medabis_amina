# Leap Year Exercise

def check_leap_year():
    try:
        # Ask the user for a year
        year = int(input("Please type in a year: "))

        # Determine if the year is a leap year
        if (year % 4 == 0 ) or (year % 400 == 0 and year % 100 == 0):
            print("That year is a leap year.")
        else:
            print("That year is not a leap year.")
    except ValueError:
        print("Please enter a valid integer for the year.")

# Run the program
check_leap_year()

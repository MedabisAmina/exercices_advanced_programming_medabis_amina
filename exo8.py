# FizzBuzz Exercise

def fizzbuzz():
    try:
        # Ask the user for a number
        number = int(input("Number: "))

        # Determine the output based on divisibility
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        # No output if not divisible by 3 or 5
    except ValueError:
        print("Please enter a valid integer.")

# Run the program
fizzbuzz()

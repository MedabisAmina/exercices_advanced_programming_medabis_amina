# Determine the Faster Runner

def determine_faster_runner():
    try:
        # Get details of the first runner
        print("Runner 1:")
        name1 = input("Name: ").strip()
        time1 = float(input("Time (in seconds): "))

        # Get details of the second runner
        print("Runner 2:")
        name2 = input("Name: ").strip()
        time2 = float(input("Time (in seconds): "))

        # Determine which runner is faster or if their times are the same
        if time1 < time2:
            print(f"The faster runner is {name1}")
        elif time2 < time1:
            print(f"The faster runner is {name2}")
        else:
            print(f"{name1} and {name2} have the same time")
    except ValueError:
        print("Please enter valid numeric values for the times.")

# Run the program
determine_faster_runner()

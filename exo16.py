def update_list():
    numbers = [1, 2, 3, 4, 5]
    print("Initial list:", numbers)

    while True:
        try:
            # Prompt the user for an index
            index = int(input("Enter index (-1 to quit): "))
            if index == -1:
                break

            # Validate the index range
            if index < 0 or index >= len(numbers):
                print("Invalid index. Please enter a value between 0 and", len(numbers) - 1)
                continue

            # Prompt the user for a new value
            new_value = input("Enter new value: ")
            if not new_value.isdigit():
                print("Invalid input. Please enter a numeric value.")
                continue

            # Update the list
            numbers[index] = int(new_value)
            print("Updated list:", numbers)

        except ValueError:
            print("Invalid input. Please enter an integer for the index.")

    print("Program exited.")

# Run the function
update_list()

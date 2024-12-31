def interactive_list_operations():
    numbers = [1, 2, 3, 4, 5]
    print("Initial List:", numbers)

    while True:
        print("\nMenu:")
        print("1. Append")
        print("2. Insert")
        print("3. Pop")
        print("4. Remove")
        print("5. Sort")
        print("6. Reverse")
        print("7. Search")
        print("8. Save to File")
        print("9. Load from File")
        print("10. Quit")

        try:
            choice = int(input("Choose an option: "))

            if choice == 1:  # Append
                value = int(input("Enter value to append: "))
                numbers.append(value)

            elif choice == 2:  # Insert
                value = int(input("Enter value to insert: "))
                index = int(input("Enter index: "))
                if 0 <= index <= len(numbers):
                    numbers.insert(index, value)
                else:
                    print("Invalid index.")

            elif choice == 3:  # Pop
                if numbers:
                    index = int(input("Enter index to pop (-1 for last): "))
                    if index == -1:
                        numbers.pop()
                    elif 0 <= index < len(numbers):
                        numbers.pop(index)
                    else:
                        print("Invalid index.")
                else:
                    print("List is empty. Nothing to pop.")

            elif choice == 4:  # Remove
                value = int(input("Enter value to remove: "))
                if value in numbers:
                    numbers.remove(value)
                else:
                    print("Value not found in the list.")

            elif choice == 5:  # Sort
                numbers.sort()

            elif choice == 6:  # Reverse
                numbers.reverse()

            elif choice == 7:  # Search
                value = int(input("Enter value to search: "))
                if value in numbers:
                    print(f"Value {value} found at index {numbers.index(value)}.")
                else:
                    print("Value not found.")

            elif choice == 8:  # Save to File
                filename = input("Enter filename to save the list: ")
                with open(filename, 'w') as file:
                    file.write(','.join(map(str, numbers)))
                print("List saved to file.")

            elif choice == 9:  # Load from File
                filename = input("Enter filename to load the list: ")
                try:
                    with open(filename, 'r') as file:
                        content = file.read()
                        numbers = list(map(int, content.split(',')))
                    print("List loaded from file.")
                except (FileNotFoundError, ValueError):
                    print("Error loading file. Ensure the file exists and is formatted correctly.")

            elif choice == 10:  # Quit
                print("Exiting program.")
                break

            else:
                print("Invalid option. Please choose a valid option.")

            print("Updated List:", numbers)

        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the program
interactive_list_operations()

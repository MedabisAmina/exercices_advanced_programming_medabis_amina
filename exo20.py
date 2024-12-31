def sorted_list_builder():
    import statistics

    user_list = []
    print("Enter numbers to add to the list (enter 0 to stop):")

    while True:
        try:
            number = int(input("Enter a number: "))
            
            if number == 0:
                break

            user_list.append(number)
            print("Current List:", user_list)
            print("Sorted List (Ascending):", sorted(user_list))

        except ValueError:
            print("Invalid input. Please enter an integer.")

    if user_list:
        print("\nFinal Statistics:")
        print("Current List:", user_list)
        print("Sorted List (Ascending):", sorted(user_list))
        print("Sorted List (Descending):", sorted(user_list, reverse=True))
        print("Mean:", round(statistics.mean(user_list), 2))
        print("Median:", statistics.median(user_list))

        save_option = input("Would you like to save the list to a file? (yes/no): ").strip().lower()
        if save_option == 'yes':
            filename = input("Enter the filename: ").strip()
            with open(filename, 'w') as file:
                file.write(','.join(map(str, user_list)))
            print(f"List saved to {filename}.")

# Run the program
sorted_list_builder()

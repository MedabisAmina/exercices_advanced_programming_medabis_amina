def unique_word_counter():
    unique_words = set()
    total_words = 0

    print("Enter words (a duplicate word will end the program):")

    while True:
        word = input("Enter a word: ").strip()
        total_words += 1

        if word in unique_words:
            print(f"You typed in {len(unique_words)} unique words.")
            print(f"Total words entered: {total_words - 1}")
            print("Unique words (alphabetically):", sorted(unique_words))

            save_option = input("Would you like to save the unique words to a file? (yes/no): ").strip().lower()
            if save_option == 'yes':
                filename = input("Enter the filename: ").strip()
                with open(filename, 'w') as file:
                    for w in sorted(unique_words):
                        file.write(w + '\n')
                print(f"Unique words saved to {filename}.")
            break

        unique_words.add(word)

# Run the program
unique_word_counter()

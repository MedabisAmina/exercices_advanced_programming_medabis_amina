# Palindrome Checker

def palindrome_checker():
    # Request input from the user
    word = input("Please type a word: ").strip()

    # Initialize a flag to check if it's a palindrome
    is_palindrome = True

    # Loop through the first half of the word
    for i in range(len(word) // 2):
        # Compare characters from the start and the end using negative indexing
        if word[i] != word[-(i + 1)]:
            is_palindrome = False
            break

    # Output the result
    if is_palindrome:
        print("Yes, it's a palindrome.")
    else:
        print("No, it's not a palindrome.")

# Run the program
palindrome_checker()

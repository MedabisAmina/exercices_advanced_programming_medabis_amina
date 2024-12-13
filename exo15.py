# Check for Vowels in a String

def check_vowels():
    # Ask the user for a string in lowercase
    user_input = input("Please type in a string: ").strip()

    # Vowels to check
    vowels = ['a', 'e', 'o']

    # Check each vowel and print whether it's found or not
    for vowel in vowels:
        if vowel in user_input:
            print(f"{vowel} found")
        else:
            print(f"{vowel} not found")

# Run the program
check_vowels()

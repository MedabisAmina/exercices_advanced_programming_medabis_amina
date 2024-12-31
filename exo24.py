def anagrams(str1, str2):
    # Remove spaces and convert to lowercase to ensure case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Taking input from the user
str1 = input("Please enter the first word: ")
str2 = input("Please enter the second word: ")

# Calling the function and printing the result (True or False)
print(anagrams(str1, str2))

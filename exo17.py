# Initialize empty lists
numbers = []
shoe_sizes = []

# Append items to the numbers list
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

# Append items to the shoe_sizes list using a loop
for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)

# Print both lists with descriptive labels
print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)

# Bonus: Add duplicate values to numbers
numbers.append(3)  # Duplicate value

# Handle duplicates in numbers (optional: remove duplicates)
numbers_no_duplicates = list(set(numbers))  # Removes duplicates but does not maintain order

# Create a third list combining numbers and shoe_sizes
combined_list = numbers + shoe_sizes

# Print bonus results
print("Numbers List with Duplicates:", numbers)
print("Numbers List without Duplicates:", numbers_no_duplicates)
print("Combined List:", combined_list)

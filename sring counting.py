# Input list
example_list = [1, 'hello', 3.5, 'world', True, 'Python', 42]

# Initialize the counter
count = 0

# Iterate through the list and check for strings
for item in example_list:
    if type(item) == str:  # Check if the item is a string
        count += 1

# Print the result
print(f"Number of strings in the list: {count}")


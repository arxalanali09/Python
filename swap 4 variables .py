# Initialize variables
a = 1
b = 2
c = 3
d = 4

print("Before swapping:", a, b, c, d)


temp_a = a
a = d
d = temp_a

temp_b = b
b = c
c = temp_b

# Print the swapped variables
print("After swapping:", a, b, c, d)
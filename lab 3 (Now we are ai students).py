filename = "student.txt"

with open(filename, "a") as file:  # Open the file in append mode
    file.write("Now we are AI students\n")

print(f'Message appended successfully to {filename}')

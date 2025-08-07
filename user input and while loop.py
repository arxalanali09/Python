correct_password = "ABC123"
user_input = ""

while user_input != correct_password:
    user_input = input("Enter the password: ")
    if user_input != correct_password:
        print("Incorrect password. Try again.")

print("Access granted!")

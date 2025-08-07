# Known username and password
known_username = "admin"
known_password = "1234"

# Prompt the user for credentials
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check credentials
if username == known_username and password == known_password:
    print("Welcome!")
else:
    print("I don’t know you.")

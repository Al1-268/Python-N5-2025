password = input("Please enter your password: ")
while len(password) < 8:
    print("Error, try again. password must be at least 8 characters long.")
    password = input("Please enter your password: ")
print("Password accepted.")

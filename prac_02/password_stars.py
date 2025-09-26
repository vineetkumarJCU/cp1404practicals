MINIMUM_LENGTH = 8

password = input("Enter Password:")
while len(password) < 8:
    print(f"Password should be {MINIMUM_LENGTH} characters long")
    password = input("Enter Password:")
if len(password) > 8:
    print("*"*len(password))

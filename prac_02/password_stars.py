MINIMUM_LENGTH = 8

def main():
    password = input("Enter Password:")
    while len(password) < 8:
        print(f"Password should be {MINIMUM_LENGTH} characters long.")
        password = input("Enter Password:")
    print("*"*len(password))

main()

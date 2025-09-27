MINIMUM_LENGTH = 8

def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter Password:")
    while len(password) < 8:
        print(f"Password should be {MINIMUM_LENGTH} characters long.")
        password = input("Enter Password:")
    return password


main()

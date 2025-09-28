MINIMUM_LENGTH = 8 # Minimum length of password

def main():
    """Main function to get and print password"""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print the asterisks based on the password length"""
    print("*" * len(password))


def get_password():
    """Ask the user for password until they enter valid password with required length"""
    password = input("Enter Password:")
    while len(password) < 8:
        print(f"Password should be {MINIMUM_LENGTH} characters long.")
        password = input("Enter Password:")
    return password


main()

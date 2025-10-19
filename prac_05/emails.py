"""
Emails File
Estimate: 15 minutes
Actual: 26 minutes
"""

def main():
    """Store users emails and names in a dictionary."""
    email_to_name = get_emails_and_names()
    display_emails(email_to_name)


def get_emails_and_names():
    """Prompt user for emails and return a dictionary."""
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        name = " ".join(email.split("@")[0].split(".")).title()
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().upper()
        if confirmation not in ("", "Y"):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ").strip()
    return email_to_name


def display_emails(email_to_name):
    """Print all stored names and emails."""
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
"""
Emails File
Estimate: 15 minutes
Actual:
"""

def main():
    """Store users emails and names in a dictionary."""
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        name = " ".join(email.split("@")[0].split(".")).title()
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().upper()
        if confirmation not in ("", "Y"):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()

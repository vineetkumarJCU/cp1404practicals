"""
CP1404/CP5632 Practical
Project Management Program
Estimate: 90 minutes
Actual:
"""

DEFAULT_FILENAME = "projects.txt"


def main():
    """Main function to run the Project Management Program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    choice = display_menu()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")

        choice = display_menu()

    print("Thank you for using custom-built project management software.")


def display_menu():
    """Display the menu and return user choice."""
    print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
          "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
    return input(">>> ").upper()


main()

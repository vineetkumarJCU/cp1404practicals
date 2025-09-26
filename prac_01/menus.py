name = input("Enter Name: ")
MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)

choice = input("Enter your choice: ")
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("Enter your choice: ")
print("Finished")

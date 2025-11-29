def main():
    title = input("Enter page title: ").strip()
    while title != "":
        print(f"Looking up: {title}")
        title = input("Enter page title: ").strip()
    print("Thank you.")


main()

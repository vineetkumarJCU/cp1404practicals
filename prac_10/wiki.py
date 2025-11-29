import wikipedia

def main():
    title = input("Enter page title: ").strip()
    while title != "":
        page = wikipedia.page(title, autosuggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
        print()
        title = input("Enter page title: ").strip()
    print("Thank you.")


main()

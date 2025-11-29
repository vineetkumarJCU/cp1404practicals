"""
CP1404 Practical 10
Wikipedia Practical Exercise
"""

import wikipedia

def main():
    """Prompt user for a Wikipedia page title and display its details."""
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following:")
            print(e.options)
        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        print()
        title = input("Enter page title: ").strip()
    print("Thank you.")


main()

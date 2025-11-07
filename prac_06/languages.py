"""
CP1404: Practical 06
Estimate Time: 25 minutes
Actual Time: 42 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    """Create and display ProgrammingLanguage objects."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()

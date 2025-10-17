"""
Word Occurrences
Estimate: 20 minutes
Actual:   28 minutes
"""

def main():
    """Count and display word occurrences in a given text."""
    text = input("Text: ")
    word_to_count = {}
    words = text.split()

    # Count each word occurrence
    for word in words:
            try:
                word_to_count[word] += 1
            except KeyError:
                word_to_count[word] = 1

    # Find width of the longest word for alignment
    max_word_width = max(len(word) for word in word_to_count)

    # Print sorted word counts
    for word, count in sorted(word_to_count.items()):
        print(f"{word:{max_word_width}} : {count}")


main()

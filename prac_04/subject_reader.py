"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename=FILENAME):
    """Read subjects from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the subjects into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)
    input_file.close()
    return subjects

def display_subjects(subjects):
    """Display subject details."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
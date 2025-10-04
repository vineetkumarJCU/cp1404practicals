"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- When a user enters something other than an integer then a value error happens.
for example: hello, $, {, nineteen
2. When will a ZeroDivisionError occur?
- When a user enters 0 as the denominator a ZeroDivisionError occurs.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- Yes, by adding a while loop to keep asking for input until it's a non-zero denominator.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator can't be 0. Please try again!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
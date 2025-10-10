"""
Warm-up Exercise
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# Recorded answers to the questions before running in console
# numbers[0] -> 3
# numbers[-1] -> 2
# numbers[3] -> 1
# numbers[:-1] -> [3, 1, 4, 1, 5, 9]
# numbers[3:4] -> [1]
# 5 in numbers -> True
# 7 in numbers -> False
# "3" in numbers -> False
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Question 1- change the first element to "ten"
numbers[0] = "ten"

# Question 2- change the last element to 1
numbers[-1] = 1

# Question 3- print all the elements in numbers except first two
print(numbers[2:])

# Question 4- print whether 9 is an element of numbers
print(9 in numbers)


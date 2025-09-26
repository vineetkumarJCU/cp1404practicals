for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Part a) count in 10s from 0 to 100
for number in range(0, 110, 10):
    print(number, end=' ')
print()

# Part b) Count down from 20 to 1
for countdown_number in range(20, 0, -1):
    print(countdown_number, end=' ')
print()

# Part c) print number of stars
number_of_stars = int(input("Enter number of stars: "))
for i in range(number_of_stars):
    print("*", end=' ')
print()

# Part d) print lines of increasing stars
number_of_stars = int(input("Enter number of stars: "))
for i in range(number_of_stars):
    for j in range(0,i+1):
        print("*", end=' ')
    print('\n')
print()
"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
Sales = float(input("Enter the sales: $"))
while Sales <= 0:
    print("Invalid Input")
    Sales = float(input("Enter the sales: $"))

if Sales < 1000:
        bonus = Sales * 0.1
        print("Your bonus is $", bonus)
else:
        bonus = Sales * 0.15
        print("Your bonus is $", bonus)
        Sales = float(input("Enter the sales: $"))
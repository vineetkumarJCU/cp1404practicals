MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    print(MENU)
    choice: str = input(">").upper()
    while choice != "Q":
        if choice == "G":
            score: float = get_valid_score()
        elif choice == "P":
            result: str = get_result(score)
            print(f"Score of {score} is {result}")
        elif choice == "S":
            print_stars(score)
        else:
             print("Invalid Choice")
        print(MENU)
        choice = input(">").upper()
    print("Thank you for using this program!")


def get_valid_score() -> float:
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = float(input("Enter score: "))
    return score

def get_result(score: float) -> str:
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score: float) -> None:
    print("*"*int(score))

main()
"""
CP1404/CP5632 Practical
Project Management Program
Estimate: 90 minutes
Actual:
"""

from datetime import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"


def main():
    """Main function to run the Project Management Program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    choice = display_menu()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")

        choice = display_menu()

    print("Thank you for using custom-built project management software.")


def display_menu():
    """Display the menu and return user choice."""
    print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
          "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
    return input(">>> ").upper()


def load_projects(filename):
    projects = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header line
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(filename, projects):
    with open(filename, "w", encoding="utf-8-sig") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                  f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(complete):
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered = [project for project in projects if project.start_date >= filter_date]
    filtered.sort(key=get_start_date)
    for project in filtered:
        print(project)


def get_start_date(project):
    return project.start_date


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yy): ")
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Select and update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")
    project.update(new_completion, new_priority)



main()

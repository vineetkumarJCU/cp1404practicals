"""
CP1404/CP5632 Practical
Project File
Estimate: 25 minutes
Actual: 40 minutes
"""

class Project:
    """Represent a project with its key details."""


    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage


    def __str__(self):
        """Return a string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare projects by priority for sorting."""
        return self.priority < other.priority


    def is_complete(self):
        """Return True if the project is complete."""
        return self.completion_percentage == 100

    def update(self, new_completion=None, new_priority=None):
        """Update completion percentage and/or priority."""
        if new_completion not in ("", None):
            self.completion_percentage = int(new_completion)
        if new_priority not in ("", None):
            self.priority = int(new_priority)




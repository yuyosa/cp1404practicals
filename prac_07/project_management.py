import datetime
import csv
from project import Project
menu = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project")
print("Welcome to Pythonic Project Management")
print("Loaded 5 projects from projects.txt")

def main():
    filename = "projects.txt"
    projects = load_project(filename)
    print(menu)
    choice = input("<<<").upper()
    while choice !="Q":
        if choice == "D":
            display_project(projects)

        elif choice == "U":
            update_project(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "F":
            filter_projects(projects)

        print(menu)
        choice = input("<<<").upper()
    print("Would you like to save to projects.txt? no, I think not.")
    print("Thank you for using custom-built project management software.")
def load_project(filename):
    projects = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) ==5:
                name, start, priority,cost, completion = row
                start_date = datetime.datetime.strptime(start.strip(), "%d/%m/%Y")
                projects.append(Project(name, start_date, int(priority), float(cost), int(completion)))
    return projects

def display_project(projects):
    projects_sorted = sorted(projects, key=lambda x: int(x.priority))
    incomplete_projects = [project for project in projects_sorted if int(project.completion) < 100]
    completed_projects = [project for project in projects_sorted if int(project.completion) == 100]

    if incomplete_projects:
        print("Incomplete projects: ")
        for project in incomplete_projects:
            print(f"  {project}")

    if completed_projects:
        print("Completed projects: ")
        for project in completed_projects:
            print(f"  {project}")

def update_project(projects):
    projects_sorted = sorted(projects, key=lambda x: x.name)
    for i, project in enumerate(projects_sorted):
        print(f"{i} {project}")

    index = int(input("Project choice:"))
    project = projects_sorted[index]
    print(project)
    new_completion = int(input("New Percentage: "))
    project.completion = new_completion
    print("New Priority:")

def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(start_date.strip(), "%d/%m/%Y")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost, completion)
    projects.append(new_project)
#ss

def filter_projects(projects):
    filter_date = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(filter_date.strip(), "%d/%m/%Y")
    filtered_projects = [project for project in projects if project.start >= filter_date]
    print("Filtered projects: ")
    for project in filtered_projects:
        print(f"  {project}")

main()
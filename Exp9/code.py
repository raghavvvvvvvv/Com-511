class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

# Get user input for manager
manager_name = input("Enter manager's name: ")
manager_id = int(input("Enter manager's employee ID: "))
manager_department = input("Enter manager's department: ")

# Get user input for developer
developer_name = input("Enter developer's name: ")
developer_id = int(input("Enter developer's employee ID: "))
programming_language = input("Enter developer's programming language: ")

# Create instances of Manager and Developer classes
manager = Manager(manager_name, manager_id, manager_department)
developer = Developer(developer_name, developer_id, programming_language)

# Display employee information
print("\nManager Information:")
manager.display_info()
print("\nDeveloper Information:")
developer.display_info()

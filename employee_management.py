class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

def list_employees_by_department(employees, department):
    return [e.name for e in employees if e.department == department]

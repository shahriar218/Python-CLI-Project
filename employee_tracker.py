import os

class Employee:
    def __init__(self, emp_id, name, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id},{self.name},{self.designation},{self.salary}"

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
        self.employees = []
        self.load_employees()

    def load_employees(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    emp_id, name, designation, salary = line.strip().split(",")
                    self.employees.append(Employee(emp_id, name, designation, salary))

    def save_employees(self):
        with open(self.filename, "w") as file:
            for emp in self.employees:
                file.write(str(emp) + "\n")

    def add_employee(self, emp_id, name, designation, salary):
        self.employees.append(Employee(emp_id, name, designation, salary))
        self.save_employees()

    def update_employee(self, emp_id, name=None, designation=None, salary=None):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                if name: emp.name = name
                if designation: emp.designation = designation
                if salary: emp.salary = salary
                self.save_employees()
                return True
        return False

    def delete_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]
        self.save_employees()

    def view_employees(self):
        for emp in self.employees:
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Designation: {emp.designation}, Salary: {emp.salary}")

    def search_employee(self, query):
        results = [emp for emp in self.employees if query.lower() in emp.name.lower() or query.lower() in emp.designation.lower()]
        for emp in results:
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Designation: {emp.designation}, Salary: {emp.salary}")

def main():
    manager = EmployeeManager()

    while True:
        print("\nEmployee Tracker CLI")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. View All Employees")
        print("5. Search Employee")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            designation = input("Enter Designation: ")
            salary = input("Enter Salary: ")
            manager.add_employee(emp_id, name, designation, salary)
            print("Employee added successfully!")
        elif choice == "2":
            emp_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name (leave blank to skip): ")
            designation = input("Enter new Designation (leave blank to skip): ")
            salary = input("Enter new Salary (leave blank to skip): ")
            if manager.update_employee(emp_id, name or None, designation or None, salary or None):
                print("Employee updated successfully!")
            else:
                print("Employee not found!")
        elif choice == "3":
            emp_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(emp_id)
            print("Employee deleted successfully!")
        elif choice == "4":
            print("All Employees:")
            manager.view_employees()
        elif choice == "5":
            query = input("Enter name or designation to search: ")
            manager.search_employee(query)
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

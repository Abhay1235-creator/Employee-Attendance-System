import os
import csv
from attendance import check_in, check_out, view_attendance_history

print("#############Employee Attendance System################")

print('''Welcome
      1. Register Employee
      2. Employee Login
      3. Admin Login
      4. Exit''')

choice = input("Enter your choice: ")
ADMIN_KEY = "LPU2026" 

def generate_employee_id(name, department):

    if not os.path.exists("employees.csv"):
        emp_no = 1
    
    else: 
        with open("employees.csv", "r") as file:
            lines = file.readlines()
            emp_no = len(lines)+1
            emp_id = (
                name[:3].upper()
                + department[:2].upper()
                + f"{emp_no:02d}"
                )
    
        return emp_id

def register_employee():
    name = input("Enter employee name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    department = input("Enter department: ")
    emp_id = generate_employee_id(name, department)
    password = input("Enter password: ")
    
    with open("employees.csv", "a") as file:
        file.write(f"{emp_id},{name},{dob},{department},{password}\n")
    
    print("Employee registered successfully!")
    print("Welcome to the Employee Attendance System, " + name + "!")
    print("Your Employee ID is: ", emp_id)

def employee_login():
    emp_id = input("Enter Employee ID: ")
    password = input("Enter Password: ")

    with open("employees.csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            emp_data = line.strip().split(",")
            if emp_data[0] == emp_id and emp_data[4] == password:
                print("Login successful!")
                print("Welcome Back", emp_data[1])
                employee_menu(emp_data[0], emp_data[1])
                return
            
        print("Invalid Employee ID or Password.")

def employee_menu(emp_id, name):
    print('''Employee Menu
          1. Check In
          2. Check Out
          3. View Attendance
          4. Logout''')
    
    menu_choice = input("Enter your choice: ")

    if menu_choice == '1':
        return check_in(emp_id)
    elif menu_choice == '2':
        return check_out(emp_id)
    elif menu_choice == '3':
        return view_attendance_history(emp_id)
    elif menu_choice == '4':
        print("Logging out...")
        return

def admin_login():

    emp_id = input("Enter employee Id: ")
    admin_key = input("Enter Admin Key: ")
    password = input("Enter Password: ")

    with open("employees.csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            emp_data = line.strip().split(",")
            if (
                emp_data[0] == emp_id
                and admin_key == ADMIN_KEY
                and emp_data[4] == password
            ):
                print("Admin login successful!")
                print("Welcome Back", emp_data[1])
                admin_dashboard()
                return
            
        print("Invalid Employee ID or Password.")

def view_all_employees():
    try:
        with open("employees.csv", "r") as file:
            lines = file.readlines()

            for line in lines:
                emp_data = line.strip().split(",")
                print(f"""
                      Employee ID: {emp_data[0]}
                      Name: {emp_data[1]}
                      Date of Birth: {emp_data[2]}
                      Department: {emp_data[3]}
                      """)
    
    except FileNotFoundError:
        print("Employee records file not found.")

def search_employee_by_id():

    try:
        emp_id = input("Enter Employee ID to search: ")
        with open("employees.csv", "r") as file:
            lines = file.readlines()
            found = False

            for line in lines:
                emp_data = line.strip().split(",")
                if emp_data[0] == emp_id:
                    found = True
                    print(f"""
                          Employee ID: {emp_data[0]}
                          Name: {emp_data[1]}
                          Date of Birth: {emp_data[2]}
                          Department: {emp_data[3]}
                          """)
                    break
            
            if not found:
                print("Employee not found.")
    except FileNotFoundError:
        print("Employee records file not found.")

def search_employee_by_department():
    try:

        department = input("Enter Department to search: ")
        with open("employees.csv", "r") as file:
            lines = file.readlines()
            found = False

            for line in lines:
                emp_data = line.strip().split(",")
                if emp_data[3].lower() == department.lower():
                    found = True
                    print(f"""
                          Employee ID: {emp_data[0]}
                          Name: {emp_data[1]}
                          Date of Birth: {emp_data[2]}
                          Department: {emp_data[3]}
                          """)
            
            if not found:
                print("No employees found in this department.")

    except FileNotFoundError:
        print("Employee records file not found.")

def view_all_attendance_records():
    try:
        with open("attendance.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)

            displayed = set()

            for line in reader:
                employee_id = line[0]
                if employee_id not in displayed:
                    displayed.add(employee_id)
                    print(f"""
                          Employee ID: {line[0]}
                          No. of Present Days: {count_present_days(line[0])}
                          """)
    
    except FileNotFoundError:
        print("Attendance records file not found.")

def count_present_days(employee_id):
    present_days = set()

    with open("attendance.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for line in reader:
            if(
                line[0] == employee_id
                and line[2] != ""
                and line[3] != ""
            ):
                present_days.add(line[1])
            
    return len(present_days)

def admin_dashboard():
    print(''' Admin Dashboard
          1. View All Employees
          2. Search Employee by ID
          3. Search Employee by Department
          4. View All Attendance Records
          5. Logout''')
    
    choice_ad = input("Enter your choice: ")

    if choice_ad == '1':
        view_all_employees()

    elif choice_ad == '2':
        search_employee_by_id()
    
    elif choice_ad == '3':
        search_employee_by_department()
    
    elif choice_ad == '4':
        view_all_attendance_records()
    
    else:
        print("Logging out...")
        return

if choice == '1':
    register_employee()
elif choice == '2':
    employee_login()
elif choice == '3':
    admin_login()
elif choice == '4':
    print("You are exiting the system. Goodbye!")
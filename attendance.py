from datetime import datetime
import csv

def check_in(employee_id):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    with open("attendance.csv", "a") as file:
        file.write(f"{employee_id},{date},{time},\n")
    
    print("Check-in successful for employee ID:", employee_id)
    print("Employee checked in at:", date, "," ,time)

def check_out(employee_id):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    rows = [] 
    with open("attendance.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 4:
                if (
                    row[0].strip() == employee_id
                    and row[1].strip() == date
                    and row[3].strip() == ""
                ):
                    row[3] = time
            
            rows.append(row)

    with open("attendance.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Check-out successful for employee ID:", employee_id)
    print("Employee checked out at:", date, "," ,time)

def view_attendance_history(employee_id):
    found = False

    try:
        with open("attendance.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            print(f"Attendance history for employee ID: {employee_id}")

            for row in reader:
                if row[0] == employee_id:
                    found = True

                    print(f"""
                          Date: {row[1]}
                          Check-in Time: {row[2]}
                          Check-out Time: {row[3]}
                          """)
    
    except FileNotFoundError:
        print("Attendance history file not found.")
        
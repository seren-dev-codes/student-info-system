import os

class Student:
    def __init__(self, student_id, first_name, last_name, gpa=None):  # None: Grade not assigned yet
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
    
    def set_gpa(self, gpa):
        if 0 <= gpa <= 100:
            self.gpa = gpa
        else:
            print("Invalid grade range (must be between 0 and 100).")
    
    def display_info(self):   
        result = (
            f"ID: {self.student_id} - {self.first_name} {self.last_name}, "
            f"GPA: {self.gpa if self.gpa is not None else 'No grade assigned'}"
        )
        return result

                  
def display_menu():
    print(""" 
   ____  _          _   ____  _ _       _    _____ _     _                 _ 
  / __ \| |        | | |  _ \(_) |     (_)  / ____(_)   | |               (_)
 | |  | | | ___   _| | | |_) |_| | __ _ _  | (___  _ ___| |_ ___ _ __ ___  _ 
 | |  | | |/ / | | | | |  _ <| | |/ _` | |  \___ \| / __| __/ _ \ '_ ` _ \| |
 | |__| |   <| |_| | | | |_) | | | (_| | |  ____) | \__ \ ||  __/ | | | | | |  V2.0
  \____/|_|\_\\__,_|_| |____/|_|_|\__, |_| |_____/|_|___/\__\___|_| |_| |_|_|
                                   __/ |                                     
                                  |___/                                      
    """)
    print("\nStudent Information System")
    print("- - - - - - - - - - - - -")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. List All Students")
    print("4. Enter Student Grade")
    print("5. Display Student Info")
    print("6. Show Overall School Average")
    print("7. Search Student by Name")
    print("8. Filter Students (Pass/Fail)")
    print("9. Exit")


def load_students_from_file(file_path):
    students = {}
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                student_id, first_name, last_name, gpa = line.split(",")
                if gpa == "None":
                    students[student_id] = Student(student_id, first_name, last_name)
                else:
                    students[student_id] = Student(student_id, first_name, last_name, float(gpa))
    return students

def save_students_to_file(file_path, students):
    folder = os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    with open(file_path, "w", encoding="utf-8") as file:
        for student in students.values():
            file.write(f"{student.student_id},{student.first_name},{student.last_name},{student.gpa}\n")  
            

def calculate_school_average(students):
    if len(students) == 0:
        print("Cannot calculate average: No students registered!")
        return
    
    total = 0
    graded_student_count = 0

    for student in students.values():
        if student.gpa is not None:
            total += student.gpa
            graded_student_count += 1
    
    if graded_student_count > 0:
        overall_average = total / graded_student_count
        print(f"Overall School GPA Average: {overall_average:.2f}")
    else:
        print("No student grades have been entered yet.")

def search_by_name(students):
    query = input("Enter name or surname to search: ").strip().lower()
    matches = [s for s in students.values() if query in f"{s.first_name} {s.last_name}".lower()]

    if matches:
        print(f"\n--- Search Results for '{query}' ---")
        for student in matches:
            print(student.display_info())
    else:
        print("No students found matching the search criteria.")

def filter_by_status(students):
    print("\n1. Passing Students (GPA >= 50)")
    print("2. Failing Students (GPA < 50)")
    choice = input("Select an option (1-2): ")

    filtered = []
    if choice == "1":
        filtered = [s for s in students.values() if s.gpa is not None and s.gpa >= 50]
    elif choice == "2":
        filtered = [s for s in students.values() if s.gpa is not None and s.gpa < 50]
    else:
        print("Invalid option!")
        return

    if filtered:
        print("\n--- Filter Results ---")
        for student in filtered:
            print(student.display_info())
    else:
        print("No students matched the selected filter.")

def main():
    file_path = "students.txt"
    students = load_students_from_file(file_path)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            if student_id in students:
                print("This student ID already exists!")
            else:
                students[student_id] = Student(student_id, first_name, last_name)
                print(f"Student {first_name} {last_name} added successfully.")

        elif choice == "2":
            student_id = input("Enter student ID to delete: ")
            if student_id in students:
                del students[student_id]
                print(f"Student ID {student_id} deleted successfully.")
            else:
                print("Student not found!")

        elif choice == "3":
            if len(students) > 0:
                print("\nStudent List:")
                for student in students.values():
                    print(student.display_info())
            else:
                print("No students registered yet!")
                    
        elif choice == "4":
            student_id = input("Enter student ID to enter grade: ")
            if student_id in students:
                try:
                    gpa = float(input("Enter GPA (0-100): "))
                    students[student_id].set_gpa(gpa)
                    print("Grade updated successfully!")
                except ValueError:
                    print("Invalid input! Please enter a numeric grade.")
            else:
                print("Student not found!")

        elif choice == "5":
            student_id = input("Enter student ID to view details: ")
            if student_id in students:
                print(students[student_id].display_info())
            else:
                print("Student not found!")

        elif choice == "6":
            calculate_school_average(students)

        elif choice == "7":
            search_by_name(students)

        elif choice == "8":
            filter_by_status(students)

        elif choice == "9":
            save_students_to_file(file_path, students)
            print("Data saved successfully. Exiting system...")
            break
        
        else:
            print("Invalid choice! Please select an option between 1 and 9.")


if __name__ == "__main__":
    main()

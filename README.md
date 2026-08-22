# Student Information System

A simple command-line **Student Information System** developed in Python. The system allows users to manage student records, enter grades, search for students, filter students by pass/fail status, and calculate the overall school average.

## Features

The system provides the following features:

1. **Add Student**

   * Add a new student with:

     * Student ID
     * First name
     * Last name
   * Prevents duplicate student IDs.

2. **Delete Student**

   * Delete a student using their student ID.

3. **List All Students**

   * Display all registered students and their grades.

4. **Enter Student Grade**

   * Assign or update a student's grade.
   * Grades must be between **0 and 100**.

5. **Display Student Info**

   * Display detailed information about a specific student.

6. **Show Overall School Average**

   * Calculate the average grade of all students who have been assigned a grade.
   * Students without a grade are not included in the calculation.

7. **Search Student by Name**

   * Search for students by first name or last name.
   * The search is case-insensitive.

8. **Filter Students (Pass/Fail)**

   * Display passing students with a grade of **50 or higher**.
   * Display failing students with a grade below **50**.

9. **Exit**

   * Save all student data to a file before exiting the program.

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* File Handling
* Dictionaries
* Exception Handling
* Command-Line Interface (CLI)

## Project Structure

```text
student-info-system/
│
├── student_system.py
├── students.txt
└── README.md
```

> `students.txt` is automatically created when the program saves student data if the file does not already exist.


```text
students.txt
```

Each student is stored in the following format:

```text
student_id,first_name,last_name,gpa
```

Example:

```text
1001,John,Doe,85.5
1002,Jane,Smith,72.0
1003,Alex,Brown,None
```

If a student has not been assigned a grade yet, their GPA is stored as `None`.

## Example Usage

When the program starts, the following menu is displayed:

```text
Student Information System
---------------------------
1. Add Student
2. Delete Student
3. List All Students
4. Enter Student Grade
5. Display Student Info
6. Show Overall School Average
7. Search Student by Name
8. Filter Students (Pass/Fail)
9. Exit
```

### Adding a Student

```text
Enter your choice: 1
Enter student ID: 1001
Enter first name: John
Enter last name: Doe

Student John Doe added successfully.
```

### Entering a Grade

```text
Enter your choice: 4
Enter student ID to enter grade: 1001
Enter GPA (0-100): 85

Grade updated successfully!
```

### Displaying Student Information

```text
ID: 1001 - John Doe, GPA: 85.0
```

### Calculating the School Average

```text
Overall School GPA Average: 78.50
```

## Grading Rules

|     Grade | Status                  |
| --------: | ----------------------- |
|  50 - 100 | Passing                 |
| 0 - 49.99 | Failing                 |
|  No grade | Not included in average |

Grades outside the **0-100** range are rejected.

## Object-Oriented Design

The project uses a `Student` class to represent each student.

The class contains the following attributes:

* `student_id`
* `first_name`
* `last_name`
* `gpa`

It also provides methods such as:

```python
set_gpa()
display_info()
```

Student objects are stored in a Python dictionary, using the student ID as the key.

## File Handling

The application automatically loads existing student records from `students.txt` when it starts.

When the user selects **Exit**, the current student data is saved back to the file.

This allows student information to persist between program executions.

## Error Handling

The program handles several types of invalid input, including:

* Duplicate student IDs
* Non-numeric grades
* Grades outside the `0-100` range
* Invalid menu selections
* Searching for non-existing students
* Deleting non-existing students

## Future Improvements

Possible improvements for future versions include:

* [ ] Add a graphical user interface (GUI)
* [ ] Use a database such as SQLite instead of a text file
* [ ] Add student email and department information
* [ ] Add sorting by name or GPA
* [ ] Add attendance tracking
* [ ] Add course-based grades
* [ ] Add login/authentication
* [ ] Export student information to CSV
* [ ] Improve input validation
* [ ] Add automated tests

## License

This project was created for educational purposes.

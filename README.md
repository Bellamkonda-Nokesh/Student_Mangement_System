# Student Management System

A simple command-line based Student Management System built in Python that allows you to manage student records with basic CRUD (Create, Read, Update, Delete) operations and data persistence.

## Features

- **Add Students**: Register new students with unique ID, name, and marks
- **View Students**: Display all registered students
- **Update Students**: Modify existing student information
- **Delete Students**: Remove students from the system
- **Data Persistence**: Save and load student data to/from JSON file
- **Input Validation**: Ensures student IDs are unique
- **Interactive Menu**: User-friendly command-line interface

## Project Structure

```
student-management-system/
├── student_management_system.py    # Main application file
├── test_cases.py                   # Unit tests
├── students.json                   # Data storage file (created automatically)
└── README.md                       # Project documentation
```

## Classes

### Student
Represents a student with the following attributes:
- `student_id`: Unique identifier for the student
- `name`: Student's name
- `marks`: Student's marks/score

### StudentManagementSystem
Main system class that handles:
- Student collection management
- CRUD operations
- Data persistence (save/load from JSON)
- User interface interactions

## Installation and Setup

1. **Prerequisites**: Python 3.6 or higher

2. **Clone or download the project files**:
   - `student_management_system.py`
   - `test_cases.py`

3. **No additional dependencies required** - uses only Python standard library

## Usage

### Running the Application

```bash
python student_management_system.py
```

### Menu Options

When you run the application, you'll see the following menu:

```
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Save Data
6. Exit
```

### Example Usage

1. **Adding a Student**:
   ```
   Enter your choice: 1
   Enter ID: 001
   Enter Name: John Doe
   Enter Marks: 85
   Student added successfully.
   ```

2. **Viewing Students**:
   ```
   Enter your choice: 2
   ID: 001, Name: John Doe, Marks: 85
   ID: 002, Name: Jane Smith, Marks: 92
   ```

3. **Updating a Student**:
   ```
   Enter your choice: 3
   Enter Student ID to update: 001
   Enter new name: John Smith
   Enter new marks: 88
   Student updated successfully.
   ```

4. **Deleting a Student**:
   ```
   Enter your choice: 4
   Enter Student ID to delete: 002
   Student deleted successfully.
   ```

## Data Persistence

- Student data is automatically loaded from `students.json` when the application starts
- Data is saved to `students.json` when you choose option 5 or exit the application
- If no previous data file exists, the system starts with an empty student list

## Testing

The project includes comprehensive unit tests in `test_cases.py`.

### Running Tests

```bash
python test_cases.py
```

### Test Coverage

The test suite covers:
- Adding students to the system
- Updating student information
- Deleting students
- Viewing students
- System initialization and setup

### Test Structure

```python
# Example test case
def test_add_student(self):
    student3 = Student("003", "Charlie", 75)
    self.system.add_student(student3)
    self.assertEqual(len(self.system.students), 3)
```

## Error Handling

- **Duplicate Student IDs**: System prevents adding students with existing IDs
- **File Not Found**: Gracefully handles missing data files on first run
- **Invalid Input**: Prompts for valid input when incorrect choices are made
- **Student Not Found**: Appropriate messages when trying to update/delete non-existent students

## Technical Details

- **Language**: Python 3.6+
- **Data Format**: JSON for persistence
- **Architecture**: Object-oriented design with separate Student and StudentManagementSystem classes
- **Testing Framework**: Python's built-in `unittest` module

## Future Enhancements

Potential improvements for the system:
- Grade calculation and GPA tracking
- Student search functionality
- Data export to CSV/Excel
- GUI interface using Tkinter or PyQt
- Database integration (SQLite/PostgreSQL)
- Student photo management
- Attendance tracking
- Report generation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions, suggestions, or issues, please create an issue in the project repository.

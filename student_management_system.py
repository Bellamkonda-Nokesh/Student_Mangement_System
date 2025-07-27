
import json

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if any(s.student_id == student.student_id for s in self.students):
            print("Student ID must be unique!")
            return
        self.students.append(student)
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students in the system.")
        for student in self.students:
            print(student)

    def update_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.name = input("Enter new name: ")
                student.marks = int(input("Enter new marks: "))
                print("Student updated successfully.")
                return
        print("Student not found!")

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]
        print("Student deleted successfully.")

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump([s.__dict__ for s in self.students], file)
        print("Data saved successfully.")

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.students = [Student(**d) for d in data]
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No previous data found.")

# Application Execution
if __name__ == "__main__":
    system = StudentManagementSystem()
    system.load_data('students.json')

    while True:
        print("\n1. Add Student\n2. View Students\n3. Update Student\n4. Delete Student\n5. Save Data\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter ID: ")
            name = input("Enter Name: ")
            marks = int(input("Enter Marks: "))
            system.add_student(Student(student_id, name, marks))
        elif choice == '2':
            system.view_students()
        elif choice == '3':
            student_id = input("Enter Student ID to update: ")
            system.update_student(student_id)
        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            system.delete_student(student_id)
        elif choice == '5':
            system.save_data('students.json')
        elif choice == '6':
            system.save_data('students.json')
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

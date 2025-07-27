
import unittest
from student_management_system import Student, StudentManagementSystem

class TestStudentManagementSystem(unittest.TestCase):
    def setUp(self):
        self.system = StudentManagementSystem()
        self.student1 = Student("001", "Alice", 85)
        self.student2 = Student("002", "Bob", 90)
        self.system.add_student(self.student1)
        self.system.add_student(self.student2)

    def test_add_student(self):
        student3 = Student("003", "Charlie", 75)
        self.system.add_student(student3)
        self.assertEqual(len(self.system.students), 3)

    def test_update_student(self):
        self.system.update_student("001")
        updated_student = next(s for s in self.system.students if s.student_id == "001")
        self.assertNotEqual(updated_student.name, "Alice")

    def test_delete_student(self):
        self.system.delete_student("002")
        self.assertEqual(len(self.system.students), 1)

    def test_view_students(self):
        self.system.view_students()
        self.assertGreater(len(self.system.students), 0)

if __name__ == "__main__":
    unittest.main()

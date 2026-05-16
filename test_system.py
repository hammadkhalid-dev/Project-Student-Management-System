import unittest

students = []



def add_student(roll, name, marks):
    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }
    students.append(student)
    return True


def search_student(roll):
    for s in students:
        if s["roll"] == roll:
            return s
    return None


def delete_student(roll):
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            return True
    return False


class TestStudentSystem(unittest.TestCase):

  
    def test_add_student(self):
        result = add_student("101", "Ali", 90)
        self.assertTrue(result)

    def test_search_student(self):
        add_student("102", "Ahmed", 85)
        student = search_student("102")
        self.assertIsNotNone(student)

    def test_delete_student(self):
        add_student("103", "Sara", 88)
        result = delete_student("103")
        self.assertTrue(result)

    def test_search_invalid_student(self):
        student = search_student("999")
        self.assertIsNone(student)


if __name__ == '__main__':
    unittest.main()
import unittest

from project.student import Student


class StudentTests(unittest.TestCase):
    name = "Jordan"
    courses = {"Python": [], "Java": []}

    def setUp(self):
        self.s = Student(self.name)
        self.s1 = Student(self.name, self.courses)

    def test_correct_init(self):
        self.assertEqual(self.name, self.s.name)
        self.assertEqual({}, self.s.courses)
        self.assertEqual(self.courses, self.s1.courses)

    def test_enroll_course_if_course_in_self_courses_should_add_notes_to_courses_and_return_str(
        self,
    ):
        self.assertEqual(
            "Course already added. Notes have been updated.",
            self.s1.enroll("Java", ("Hello", "World")),
        )
        self.assertEqual({"Python": [], "Java": ["Hello", "World"]}, self.s1.courses)

    def test_enroll_if_add_course_notes_is_equal_to_y_and_empty_str_should_add_course_and_notes(
        self,
    ):
        self.assertEqual(
            "Course and course notes have been added.",
            self.s.enroll("Java", ["Hello", "World"]),
        )
        self.assertEqual({"Java": ["Hello", "World"]}, self.s.courses)
        self.assertEqual(
            "Course and course notes have been added.",
            self.s.enroll("Python", ["Hello", "World"], add_course_notes="Y"),
        )
        self.assertEqual(
            {"Java": ["Hello", "World"], "Python": ["Hello", "World"]}, self.s.courses
        )

    def test_enroll_add_course_if_not_in_courses_and_return_str(self):
        self.assertEqual(
            "Course has been added.",
            self.s.enroll("Python", "Hello", add_course_notes="N"),
        )
        self.assertEqual({"Python": []}, self.s.courses)

    def test_leave_course_if_course_not_in_courses_raise_exeption_str(self):
        with self.assertRaises(Exception) as contex:
            self.s.leave_course("js")
        self.assertEqual(
            "Cannot remove course. Course not found.", str(contex.exception)
        )

    def test_leave_course_if_course_in_courses_remove_course_and_return_str(self):
        self.assertEqual("Course has been removed", self.s1.leave_course("Java"))
        self.assertEqual({"Python": []}, self.s1.courses)

    def test_add_notes_if_course_not_in_courses_raise_exception_str(self):
        with self.assertRaises(Exception) as contex:
            self.s.add_notes("js", "Hello")
        self.assertEqual("Cannot add notes. Course not found.", str(contex.exception))


if __name__ == "__main__":
    unittest.main()

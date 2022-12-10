from project.student import Student
from unittest import TestCase, main


class Tests(TestCase):
    def setUp(self):
        self.student = Student('good', {'abc': ['notes_str']})
        self.lazy_student = Student('lazy')

    def test_good_init_(self):
        self.assertEqual('lazy', self.lazy_student.name)
        self.assertEqual({}, self.lazy_student.courses)

        self.assertEqual('good', self.student.name)
        self.assertEqual({'abc': ['notes_str']}, self.student.courses)

    def test_enroll_student_in_course_already_added(self):
        actual = self.student.enroll('abc', 'x')

        self.assertEqual(['notes_str', 'x'], self.student.courses['abc'])
        self.assertEqual('Course already added. Notes have been updated.', actual)

    def test_enroll_new_course_with_notes(self):
        actual = self.lazy_student.enroll('Math', ['x1', 'x2'], 'Y')

        self.assertEqual({'Math': ['x1', 'x2']}, self.lazy_student.courses)
        self.assertEqual('Course and course notes have been added.', actual)

    def test_enroll_new_course_with_notes_case_2(self):
        actual = self.lazy_student.enroll('Math', [])

        self.assertEqual({'Math': []}, self.lazy_student.courses)
        self.assertEqual('Course and course notes have been added.', actual)

    def test_enroll_new_course_without_notes(self):
        actual = self.lazy_student.enroll('Math', [], 'N')

        self.assertEqual({'Math': []}, self.lazy_student.courses)
        self.assertEqual("Course has been added.", actual)

    def test_add_notes_in_a_course_that_already_exist(self):
        actual = self.student.add_notes('abc', 'new_note')

        self.assertTrue('existing', self.student.courses['abc'])
        self.assertEqual("Notes have been updated", actual)

    def test_add_notes_in_a_course_not_yet_added(self):
        with self.assertRaises(Exception) as ex:
            self.lazy_student.add_notes('not_in', ['new_note'])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_try_leaving_as_student_not_in_the_course(self):
        with self.assertRaises(Exception) as ex:
            self.lazy_student.leave_course('not_in')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_try_leaving_as_a_student_from_the_course(self):
        actual = self.student.leave_course('abc')
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", actual)


if __name__ == '__main__':
    main()

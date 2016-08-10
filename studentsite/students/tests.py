import datetime
import random
import re

from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from .factories import SAMPLE_GRADES, StudentFactory
from .models import Student


client = Client()


class CreateStudentTest(TestCase):

    def test_create_student(self):
        student = Student.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth=datetime.date(2010, 8, 15),
            grade="K",
        )

        self.assertTrue(isinstance(student, Student))
        self.assertEqual(str(student), "Doe, John - Grade K, born 8/15/2010")


class TestStudentsListView(TestCase):

    def setUp(self):
        """Create some sample students."""
        self.students = StudentFactory.create_batch(30)

    def student_names(self, students):
        """Get last, first names of students in sorted order."""
        return ["{}, {}".format(s.last_name, s.first_name).encode("utf-8") for s in sorted(students, key=lambda s: s.last_name)]

    def test_students_list_view(self):
        """Test that view responds and lists students in correct order."""
        response = client.get(reverse("students_list"))
        self.assertEqual(response.status_code, 200)

        response_names = re.findall(b"<li>(.*?) - Grade", response.content, re.MULTILINE)
        self.assertEqual(response_names, self.student_names(self.students))

    def test_filter_students_by_grade(self):
        """Test that a grade query returns only students in that grade."""
        for _ in range(0, 5):  # Try a few grades
            grade = random.choice(SAMPLE_GRADES)
            students_in_grade = [s for s in self.students if s.grade == grade]

            response = client.get(reverse("students_list"), dict(grade=grade))
            response_names = re.findall(b"<li>(.*?) - Grade", response.content, re.MULTILINE)
            self.assertEqual(response_names, self.student_names(students_in_grade))

    def test_no_students_in_grade(self):
        """Test that a message is shown when no students are found in a grade."""
        response = client.get(reverse("students_list"), dict(grade="doesnotexist"))
        self.assertIn(b"No students found.", response.content)

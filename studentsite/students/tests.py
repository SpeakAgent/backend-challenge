import datetime

from django.test import TestCase

from .models import Student


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

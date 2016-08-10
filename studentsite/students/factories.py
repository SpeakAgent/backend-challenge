import random

import faker
from factory import DjangoModelFactory, LazyAttribute, LazyFunction

from .models import Student


faker = faker.Factory.create()


SAMPLE_GRADES = ["Pre-K", "K"] + [str(i) for i in range(1, 13)]


def dob_for_grade(grade):
    """
    Generate a reasonable date of birth for a student in a specific grade,
    assuming students in kindergarten were born 5-6 years ago.
    """
    grade_number = grade
    if grade == "Pre-K":
        grade_number = -1
    elif grade == "K":
        grade_number = 0
    else:
        grade_number = int(grade)

    start = "-%dy" % (6 + grade_number)
    end = "-%dy" % (5 + grade_number)
    return faker.date_time_between(start_date=start, end_date=end).date()


class StudentFactory(DjangoModelFactory):
    """Generate a random student."""
    class Meta:
        model = Student

    first_name = LazyFunction(faker.first_name)
    last_name = LazyFunction(faker.last_name)
    date_of_birth = LazyAttribute(lambda s: dob_for_grade(s.grade))
    grade = LazyFunction(lambda: random.choice(SAMPLE_GRADES))

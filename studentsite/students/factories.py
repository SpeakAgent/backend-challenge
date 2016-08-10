import random

import faker
from factory import DjangoModelFactory, LazyAttribute, LazyFunction, post_generation

from .models import School, Student, Teacher


faker = faker.Factory.create()


SCHOOL_LEVELS = ["Elementary", "Middle", "High"]


class SchoolFactory(DjangoModelFactory):
    """Generate a random school."""
    class Meta:
        model = School

    title = LazyFunction(lambda: "{} {} School".format(faker.street_name(), random.choice(SCHOOL_LEVELS)))
    address = LazyFunction(faker.street_address)


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

    @post_generation
    def schools(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.school = random.choice(extracted)

    @post_generation
    def teachers(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            num_teachers = random.randint(min(2, len(extracted)), min(5, len(extracted)))
            for teacher in random.sample(extracted, num_teachers):
                self.teachers.add(teacher)


class TeacherFactory(DjangoModelFactory):
    """Generate a random teacher."""
    class Meta:
        model = Teacher

    first_name = LazyFunction(faker.first_name)
    last_name = LazyFunction(faker.last_name)

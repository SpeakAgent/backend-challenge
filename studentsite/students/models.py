from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class School(models.Model):
    title = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.title


@python_2_unicode_compatible  # Prevents having to also define __unicode__()
class PersonInfo(models.Model):
    """
    Abstract base class providing common functionality for models with
    `first_name` and `last_name` fields.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        abstract = True
        ordering = ['last_name', 'first_name']

    @property
    def full_name(self):
        """
        Property representing the full name in "Lastname, Firstname" format.
        """
        return "{l}, {f}".format(
            l=self.last_name,
            f=self.first_name)

    def __str__(self):
        return self.full_name


class Teacher(PersonInfo):
    pass


class Student(PersonInfo):
    dob = models.DateField("Date of birth", blank=True, null=True)

    # Using CharField for the grade could be problematic without some
    # validation, since it's used verbatim as part of a URL. In a real-world
    # application it would probably make more sense to create a separate model
    # representing a Grade, with a display name and slug. (This would also make
    # it possible to distinguish between a grade w/o any students and a 404 for
    # a grade that doesn't exist, and would prevent certain typos/user errors.)
    grade = models.CharField(max_length=20, blank=True)

    school = models.ForeignKey(
        School, related_name="students", null=True, blank=True)
    teachers = models.ManyToManyField(
        Teacher, related_name="students", blank=True)

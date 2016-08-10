from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    grade = models.CharField(null=True, max_length=20)

    def __str__(self):
        return "{l}, {f} - Grade {g}, born {dob:%-m/%-d/%Y}".format(
            l=self.last_name,
            f=self.first_name,
            g=self.grade,
            dob=self.date_of_birth)

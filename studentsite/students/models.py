from __future__ import unicode_literals
import datetime

from django.db import models


# Student model, every student have one school
# and can have one or more teachers.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=datetime.date.today)
    grade = models.CharField(max_length=1, blank=True)
    school = models.ForeignKey('students.School')
    teachers = models.ManyToManyField('students.Teacher')

    def __unicode__(self):
        return u"{l}, {f}".format(
            l=self.last_name,
            f=self.first_name)


# School model
class School(models.Model):
    title = models.CharField(max_length=100)
    address = models.TextField()

    def __unicode__(self):
        return self.title


# Teacher model
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u"{l}, {f}".format(
            l=self.last_name,
            f=self.first_name)

from __future__ import unicode_literals

from django.db import models


class PersonInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def full_name(self):
        return u"{l}, {f}".format(
            l=self.last_name,
            f=self.first_name)
    full_name.short_description = "Full name"

    def __unicode__(self):
        return self.full_name()


class School(models.Model):
    title = models.CharField(max_length=100)
    address = models.TextField()


class Teacher(PersonInfo):
    pass


class Student(PersonInfo):
    date_of_birth = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=20, blank=True)
    school = models.ForeignKey(
        School, related_name="students", null=True, blank=True)
    teachers = models.ManyToManyField(Teacher, related_name="students")

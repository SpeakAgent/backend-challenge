from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from rest_framework import serializers


@python_2_unicode_compatible
class School(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return "{l}, {f}".format(
            l=self.last_name,
            f=self.first_name)


@python_2_unicode_compatible
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    grade = models.CharField(null=True, max_length=20)

    school = models.ForeignKey(School, null=True, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return "{l}, {f} - Grade {g}, born {dob:%-m/%-d/%Y}".format(
            l=self.last_name,
            f=self.first_name,
            g=self.grade,
            dob=self.date_of_birth)


class StudentSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(source="date_of_birth")

    class Meta:
        model = Student
        fields = ("first_name", "last_name", "grade", "dob")

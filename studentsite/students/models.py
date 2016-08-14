from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    DOB = models.CharField(max_length=10)
    grade = models.CharField(max_length=2)

    def __unicode__(self):
        return u"{l}, {f} - Grade {g}, born {d}".format(
            l=self.last_name,
            f=self.first_name,
            d=self.DOB,
            g=self.grade)

class School(models.Model):
    title = models.CharField(max_length=50)
    #condense 4 following to one 4-line TextField
    address1 = models.CharField(max_length=40)
    address2 = models.CharField(max_length=40)
    address3 = models.CharField(max_length=40)
    address4 = models.CharField(max_length=40)
    
    def __unicode__(self):
        return u"{t}\n{a1}\n{a2}\n{a3}\n{a4}".format(
            t=self.title,
            a1=self.address1,
            a2=self.address2,
            a3=self.address3,
            a4=self.address4)

class Teacher(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)

    def __unicode__(self):
        return u"{l}, {f}".format(
            l=self.last_name,
            f=self.first_name)


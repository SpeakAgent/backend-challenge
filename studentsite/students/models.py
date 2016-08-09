from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    DOB = models.CharField(max_length=10)
    grade = models.CharField(max_length=1)

    def __unicode__(self):
        return u"{l}, {f}".format(
            l=self.last_name,
            f=self.first_name)

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    office = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()

    def __unicode__(self):
        return self.first_name


class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __unicode__(self):
        return self.first_name

class Course(models.Model):
    teacher = models.ForeignKey(Teacher)  # a course can have one teacher
    student = models.ManyToManyField(Students)  # a course can have many students enrolled in it

    name = models.CharField(max_length=30)
    code = models.CharField(max_length=10)
    classroom = models.CharField(max_length=10)
    times = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
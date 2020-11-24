from django.db import models

# Create your models here.

class Studentdetails(models.Model):
    studentid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    major = models.CharField(max_length=500)
    year = models.CharField(max_length=500)
    gpa = models.DecimalField(decimal_places=1, max_digits=3)

class Courseinfo(models.Model):
    courseid = models.IntegerField(primary_key=True)
    coursetitle = models.CharField(max_length=500)
    coursename = models.CharField(max_length=500)
    courseselectioncode = models.IntegerField()
    coursedepartment = models.CharField(max_length=500, default='SOME STRING')
    instructorname = models.CharField(max_length=500, default='SOME STRING')

class Enrollment(models.Model):
    studentid= models.IntegerField()
    courseid = models.IntegerField()
    coursetitle = models.CharField(max_length=500, default='SOME STRING')
    coursename = models.CharField(max_length=500)
    courseselectioncode = models.IntegerField(default=0)
    coursedepartment = models.CharField(max_length=500, default='SOME STRING')
    instructorname = models.CharField(max_length=500, default='SOME STRING')

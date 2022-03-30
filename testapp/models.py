from django.db import models


# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField()
    name= models.CharField(max_length=20)
    dob = models.DateField()
    marks = models.IntegerField()
    email = models.EmailField()
    phone_no=models.BigIntegerField()
    address= models.TextField()

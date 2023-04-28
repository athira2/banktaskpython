from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    cpassword=models.CharField(max_length=250)


class Form(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    phonenumber=models.IntegerField()
    mailid=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    district=models.CharField(max_length=250)
    branches=models.CharField(max_length=250)
    accounttype=models.CharField(max_length=250)
    materials=models.CharField(max_length=250)


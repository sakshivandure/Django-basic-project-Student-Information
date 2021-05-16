from django.db import models

# Create your models here.
class student(models.Model):
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    rollnumber= models.IntegerField()
    usn= models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    city= models.CharField(max_length=200)
    gender= models.CharField(max_length=100)
    dep= models.CharField(max_length=200)
    img= models.ImageField(upload_to='img')

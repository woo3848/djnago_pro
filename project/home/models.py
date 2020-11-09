from django.db import models

# Create your models here.

class Member(models.Model):
    userid = models.CharField(max_length=200)
    userpw = models.CharField(max_length=50)
    username= models.CharField(max_length=50)
    birth = models.CharField(max_length=30)
    phonenum = models.CharField(max_length=20)

class Board(models.Model):
    idx = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    file = models.CharField(max_length=255, null=True, blank=True)
    datetime = models.DateTimeField()
    isDeleted = models.BooleanField(default=False)
    
    


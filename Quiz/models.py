from __future__ import unicode_literals
from django.db import models
from users.models import User
from django.utils import timezone
# Create your models here.

class CareerQuiz(models.Model):
    question = models.CharField(max_length = 200)
    choice_one = models.CharField(max_length = 200,default='Difficult')
    choice_two = models.CharField(max_length = 200,default='Less Difficult')
    choice_three = models.CharField(max_length = 200,default='Neutral')
    choice_four = models.CharField(max_length = 200,default='Easy')
    qtype=models.CharField(max_length=300,default='Null')
    
    def __str__(self):
    	return self.question 


class Result(models.Model):
    User_Name=models.OneToOneField(User,on_delete=models.CASCADE)
    Interest_1=models.CharField(max_length=100,unique=False)
    Interest_2=models.CharField(max_length=100,unique=False)
    Date_Created=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.User_Name 


class StreamQuiz(models.Model):
    question = models.CharField(max_length = 200)
    choice_one = models.CharField(max_length = 200)
    choice_two = models.CharField(max_length = 200)
    choice_three = models.CharField(max_length = 200)
    choice_four = models.CharField(max_length = 200)
    qtype=models.CharField(max_length=300)
    
    def __str__(self):
        return self.question 

class SResult(models.Model):
    User_Name=models.OneToOneField(User,on_delete=models.CASCADE)
    Interest_1=models.CharField(max_length=100,unique=False)
    Interest_2=models.CharField(max_length=100,unique=False)
    Date_Created=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.User_Name 


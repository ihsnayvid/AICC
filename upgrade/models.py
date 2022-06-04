from django.db import models
from django.utils import timezone
from users.models import User
# Create your models here.
class questions(models.Model):
	q=models.CharField(max_length=200)
	op1=models.CharField(max_length=3)
	op2=models.CharField(max_length=3)

	def __str__(self):
		return self.q

class other_career(models.Model):
	career=models.CharField(max_length=100)
	datec=models.DateTimeField(default=timezone.now)
	user=models.OneToOneField(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.career
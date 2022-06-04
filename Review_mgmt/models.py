from django.db import models
from django.utils import timezone

class review(models.Model):
	email=models.CharField(max_length=30)
	feedback=models.CharField(max_length=200)
	Date_Created=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.feedback
	
# Create your models here.
# nBr2vzXbo5D9BcOu72H0o6szwRcNdmrxnGYy0D85lrk
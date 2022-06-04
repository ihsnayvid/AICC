from django.db import models
from django.utils import timezone
# Create your models here.
class chat(models.Model):
	Enter_your_Query_Here=models.CharField(max_length=100)
	date_create=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.Enter_your_Query_Here
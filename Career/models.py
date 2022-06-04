from django.db import models

# Create your models here.
class career(models.Model):
	
	Name=models.CharField(max_length=200,unique=False,default='law')
	Summary=models.TextField()
	Career_Opportunities=models.TextField()
	How_to_become=models.TextField()
	Important_Facts=models.TextField()
	Work_Description=models.TextField()
	Pros_and_Cons=models.TextField()

	def __str__(self):
		return self.Name
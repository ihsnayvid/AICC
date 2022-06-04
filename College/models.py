from django.db import models
from django_matplotlib import MatplotlibFigureField

# Create your models here.
class clg(models.Model):
	clg_name=models.CharField(max_length=200)
	clg_loc=models.CharField(max_length=200)
	clg_top_field=models.TextField()
	clg_website=models.CharField(max_length=300)
	

	def __str__(self):
		return self.clg_name
class MyModel(models.Model):
	figure=MatplotlibFigureField(figure='my_figure')


	
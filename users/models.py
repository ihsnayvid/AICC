from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
	user =models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')
		

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self,*args,**kwargs):
		super().save()
		img=Image.open(self.image.path)
		if img.height > 300 or img.width >300:
			output_size=(300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

class ProfileSummary(Profile):
    class Meta:
        proxy = True
        verbose_name = 'Profile Summary'
        verbose_name_plural = 'Profiles Summary'

class status(models.Model):
	value=models.CharField(max_length=200,unique=False)
	def __str__(self):
		return self.value

class helpp(models.Model):
	value=models.CharField(max_length=200,unique=False)
	def __str__(self):
		return self.value


class getname(models.Model):
	User_Name=models.OneToOneField(User,on_delete=models.CASCADE)
	My_Name_is=models.CharField(max_length=200)
	I_need_Help_with=models.OneToOneField(helpp,on_delete=models.CASCADE)
	I_Study_in_Class=models.CharField(max_length=2)

	def __str__(self):
		return self.My_Name_is

class add_details(models.Model):
	User_Name=models.OneToOneField(User,on_delete=models.CASCADE)
	Mobile_Number=models.CharField(max_length=10)
	Verification_Code=models.CharField(max_length=10)
	City=models.CharField(max_length=200)
	
	def __str__(self):
		return self.Mobile_Number








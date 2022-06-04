from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
class Post(models.Model):
	
	title=models.CharField(max_length=100)
	content=models.TextField()
	Date=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg',upload_to='media/profile_pics')
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail',kwargs={'pk':self.pk})

	
class comment(models.Model):
	Post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
	Message=models.CharField(max_length=500)
	Created_On=models.DateTimeField(default=timezone.now)
	User_Id=models.ForeignKey(User,on_delete=models.CASCADE)
	active=models.BooleanField(default=False)
	

	def __str__(self):
		return self.Message

	def get_absolute_url(self):
		return reverse('post_detail',kwargs={'pk':self.pk})


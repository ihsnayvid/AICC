from django import forms
from .models import comment,Post,User


class CommentForm(forms.ModelForm):
	
	class Meta:
		model=comment
		fields=['Message','Post']

class textForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['title','Date','author','image']

	
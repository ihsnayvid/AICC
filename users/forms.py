from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,getname,add_details
class UserRegisterForm(UserCreationForm):
	
	email=forms.EmailField()
	
	
	class Meta:
		model=User
		#fields=['Name','Class','Address','Phone','email','password1','password2']
		fields=['first_name','last_name','username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()
	
	class Meta:
		model=User
		fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['image']

class User2Form(forms.ModelForm):
	class Meta:
		model=getname
		fields="__all__"

class User3Form(forms.ModelForm):
	class Meta:
		model=add_details
		fields="__all__"




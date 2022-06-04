from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,User2Form,User3Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import auth
from.models import User

# Create your views here.
def register(request):
	if request.method =='POST':
		form=UserRegisterForm(request.POST)
		
		if form.is_valid():
			form.save()
			
			username=form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created! {username}!')
			return redirect('login')
	else:
		form=UserRegisterForm()
	return render(request,'users/register.html',{'form':form})
@login_required
def profile(request):
	if request.method =='POST':
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)#updating user and profile
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)
	context={
	'u_form':u_form,
	'p_form':p_form

	}

	return render(request,'users/profile.html',context)


'''def user2form_add(request):
	if request.method=='POST':
		form=User2Form(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'Data added successfully')
			return redirect('form3')
	else:
		form=User2Form()

	return render(request,'users/user2.html',{'form':form})

'''
def user3form_add(request):
	if request.method=='POST':
		form=User3Form(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'Thank You for corporating with us!')
			return redirect('quiz')
	else:
		form=User3Form()

	return render(request,'users/user3.html',{'form':form})

def login(request):
	if request.method =='POST':

		username=request.POST['username']
		password1=request.POST['password1']
		User=auth.authenticate(username=username,password=password1)
		if User is not None:
			auth.login(request,User)
			return redirect("homepage")
		else:
			messages.warning(request,"Invalid Credentials")
			return redirect('login')
	else:
		return render(request,'users/login.html')

def logout(request):
	auth.logout(request)
	return render(request,'index/home.html')


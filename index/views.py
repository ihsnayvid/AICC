from django.shortcuts import render

from django.contrib import messages
# Create your views here.
def homepage(request):
	return render(request,'index/home.html')


def classeight(request):
	return render(request,'index/8-9.html')

def classeleven(request):
	return render(request,'index/10-12.html')


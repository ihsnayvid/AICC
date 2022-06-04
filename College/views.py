from django.shortcuts import render,redirect
from .models import clg
from django.db.models import Q
from django.contrib import messages
def searchclg(request):
	if request.method=='POST':
		srch=request.POST['textbox']
		if srch:
			match=clg.objects.filter(Q(clg_top_field__icontains=srch))

			if match:
				return render(request,'College/college.html',{'sr':match})
			
		else:
			return HttpResponseRedirect('/college/')
	return render(request,'College/college.html')


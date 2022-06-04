from django.shortcuts import render
from .models import career
from django.db.models import Q
from django.contrib import messages
# Create your views here.
def careerlib(request):
	return render(request,'career/career-library.html')

def law_career(request):
	
	srch='Law'

	if srch:
		match1=career.objects.filter(Q(Summary__icontains=srch))
		
		if match1:
			return render(request,'career/law.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/law/')
	return render(request,'career/law.html')

def architecture_career(request):
	
	srch='Architecture'

	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/architecture.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/architecture/')
	return render(request,'career/architecture.html')

def pilot_career(request):
	
	srch='Aviation'

	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/pilot.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/pilot/')
	return render(request,'career/pilot.html')

def medicine_career(request):
	
	srch='Medicine'

	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/medicine.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/medicine/')
	return render(request,'career/medicine.html')
def fashion_career(request):
	
	srch='Fashion'

	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/fashion.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/fashion/')
	return render(request,'career/fashion.html')

def civil_career(request):
	
	srch='Civil Services'
	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/civil_services.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/civil_services/')
	return render(request,'career/civil_services.html')

def defense_career(request):
	
	srch='Defense'

	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/defense.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/defense/')
	return render(request,'career/defense.html')
def manage_career(request):
	
	srch='Management'

	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/management.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/manage/')
	return render(request,'career/management.html')
def computer_career(request):
	
	srch='Computer Application and IT'

	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/computer.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/computer/')
	return render(request,'career/computer.html')

def cabin_career(request):
	
	srch='Cabin  Crew'

	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/cabin.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/cabin/')
	return render(request,'career/cabin.html')

def food_career(request):
	
	srch='Food Science and Technology'

	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/food.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/food/')
	return render(request,'career/food.html')

def bank_career(request):
	
	srch='Banking'

	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/banking.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/banking')
	return render(request,'career/banking.html')

def education_career(request):
	
	srch='Entrepreneurship'

	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/entrepreneurship.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/entrepreneurship/')
	return render(request,'career/entrepreneurship.html')

def commerce_career(request):
	
	srch='Commerce'

	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/commerce.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/commerce/')
	return render(request,'career/commerce.html')

def arts_career(request):
	
	srch='Fine Arts'

	if srch:
		match1=career.objects.filter(Q(Name__icontains=srch))
		
		if match1:
			return render(request,'career/arts.html',{'sr1':match1})

	else:
		return HttpResponseRedirect('/arts/')
	return render(request,'career/arts.html')


def searchcareer(request):
	if request.method=='POST':
		srch=request.POST['textbox']
		if srch:
			match=career.objects.filter(Q(Name__icontains=srch))

			if match:
				return render(request,'career/career-search.html',{'sr':match})

			else:
				messages.error(request,f'No results found for {srch}!')
			

		else:
			return HttpResponseRedirect('/career-search/')
	return render(request,'career/career-search.html')

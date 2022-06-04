from django.shortcuts import render
from .models import questions
# Create your views here.
from code import predict_career
def advance_Quiz(request):
    question =questions.objects.all()
    count=questions.objects.all().count()
    context={'question': question,'count':count}
    return render(request,'upgrade/advance_test.html',context)

def predicts(request):
    values = list(request.POST)
    keys = list(request.POST.items())
    n=1
    newlist = values[n:]
    newkey = keys[n:]
    values_data=questions.objects.filter(pk__in = newlist).values().order_by('id')
    l=[]
    o=[]
    fc=0
   
    for i in values_data:
        fc=fc+1
        for j in newkey:
            if int(i['id']) == int(j[0]):
                o.append(j[1])
                i.update({'your_answer':j[1]})
                l.append(i)

    a=[o]
    answer=predict_career(a)
    return render(request,'upgrade/advance_result.html',{'post_data':l,'a':a,'fc':fc,'prediction':answer})

def premium_intro(request):
    return render(request,'upgrade/premium.html')

def choose_career(request):
    if request.method =="POST":
        career=request.POST['career']
    elif request.method == 'GET':
        career=""
    return render(request,'upgrade/choose_career.html',{'career':career})
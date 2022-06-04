from django.shortcuts import render,redirect
from Quiz.models import CareerQuiz,StreamQuiz
from django.contrib import messages
from reportlab.pdfgen import canvas  
from django.http import HttpResponse 
# Create your views here.
from matplotlib import pylab
from pylab import *
from PIL import Image
from io import BytesIO
import numpy as np
def SQuiz_intro(request):
	return render(request,'Quiz/streamquiz_introduction.html')

def CQuiz_intro(request):
    return render(request,'Quiz/careerquiz_introduction.html')

def Quiz_display(request):
	
	questions=CareerQuiz.objects.all()
	count=CareerQuiz.objects.all().count()
	context={'questions': questions,'count':count}
	return render(request,'Quiz/IQuiz.html',context)
    
def Stream_Quiz(request):
    questions =StreamQuiz.objects.all()
    count=StreamQuiz.objects.all().count()
    context={'questions': questions,'count':count}
    return render(request,'Quiz/streamquiz.html',context)

def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "AICC Career Report")  
    
    p.showPage()  
    p.save()  
    return response 
def StreamQuiz_result(request):
    values = list(request.POST)
    keys = list(request.POST.items())
    n=1
    newlist = values[n:]
    newkey = keys[n:]
    values_data=StreamQuiz.objects.filter(pk__in = newlist).values().order_by('id')
    l=[]
    count_science=0
    count_humanities=0
    count_commerce=0
    count_arts=0
    fc=0
    interest_1=0
    interest_2=0
    for i in values_data:
        fc=fc+1
        for j in newkey:
            if int(i['id']) == int(j[0]):
                i.update({'your_answer':j[1]})
                l.append(i)
                print(l)
                if i['your_answer'] == '1':
                    count_humanities=count_humanities+1 
                if i['your_answer'] == '2':
                    count_science=count_science+1 
                if i['your_answer'] == '3':
                    count_commerce=count_commerce+1 
                if i['your_answer'] == '4':
                    count_arts=count_arts+1 
            else:
                pass
    a=[count_humanities,count_arts,count_science,count_commerce]
    a.sort()
    interest_1=a[-1]
    interest_2=a[-2]
    print(interest_1)
    print(interest_2)
    print(count_science,count_arts,count_humanities,count_commerce)
    return render(request,'Quiz/streamquiz_result.html',{'post_data':l,'count_humanities':count_humanities,'count_science':count_science,'count_arts':count_arts,'count_commerce':count_commerce,'fc':fc,'interest_1':interest_1,'interest_2':interest_2})


'''def getimage(request):
    x=np.arange(0,2*pi,0.01)
    y=cos(x)**2
    plot(x,y)
    xlabel('X Axis')
    ylabel('Y Axis')
    title('Simple Graph')
    #grid(True)
    buffer=BytesIO()
    canvas=pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage =Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
    return HttpResponse(buffer.getvalue(),content_type='image/png')'''


def CareerQuiz_result(request):
    values = list(request.POST)
    keys = list(request.POST.items())
    n=1
    newlist = values[n:]
    newkey = keys[n:]
    values_data=CareerQuiz.objects.filter(pk__in = newlist).values().order_by('id')
    l=[]
    count=0
    fc=0
    question_type=[]
    for i in values_data:
        fc=fc+1
        for j in newkey:
            if int(i['id']) == int(j[0]):
                i.update({'your_answer':j[1]})
                l.append(i)
                
                print(i)
                if i['your_answer'] == '4':
                    count=count+1 
                    question_type.append(i['qtype'])

                
            else:
                pass
    print(count)
    print(question_type)

    return render(request,'Quiz/iquiz_result.html',{'post_data':l,'count':count,'qtype':question_type,'fc':fc})







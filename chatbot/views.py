from django.shortcuts import render
from django.http import HttpResponse
from . models import chat
from .forms import ChatForm
#from textblob import TextBlob
import nltk
from chatterbot import ChatBot
from code import ChatAnalyzer
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def chat(request):
    
    form = ChatForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            sent = form.cleaned_data.get('Enter_your_Query_Here')
            textAns = ChatAnalyzer(sent)
            context['text'] = textAns
            form.save()
            messages.success(request,'Please Wait! While we are processing your feedback!')
        else:
            form = ChatForm()
    
    context['form'] = form
    return render(request, 'chatbot/review.html', context=context)




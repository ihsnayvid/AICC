from django.shortcuts import render
from django.http import HttpResponse
from .models import review
from .forms import Review
#from textblob import TextBlob
import nltk
from code import SentimentAnalyzer
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def review(request):
    form = Review(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            sent = form.cleaned_data.get('feedback')
            textAns = SentimentAnalyzer(sent)
            context['text'] = textAns
            form.save()
            messages.success(request,'Please Wait! While we are processing your feedback!')
        else:
            form = Review()
    
    context['form'] = form
    return render(request, 'Review_mgmt/review.html', context=context)




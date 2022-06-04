from django import forms
from .models import review
class Review(forms.ModelForm):
	class Meta:
		model=review
		fields=["email","feedback"]
		
'''def clean_sentiment(self):
	sentiment=self.cleaned_data['sentiment']
	return sentiment'''
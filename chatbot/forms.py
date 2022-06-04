from django import forms
from .models import chat
class ChatForm(forms.ModelForm):
	class Meta:
		model=chat
		fields=['Enter_your_Query_Here']
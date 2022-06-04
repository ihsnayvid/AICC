from django.urls import path
from .import views

urlpatterns = [
path('squiz_intro/',views.SQuiz_intro, name='squiz'),
path('cquiz_intro/',views.CQuiz_intro, name='cquiz'),
path('quiz/',views.Quiz_display, name='iquiz'),

path('pdf/',views.getpdf, name='get-report'),
path('stream/',views.Stream_Quiz, name='Stream_Quiz'),
path('stream-result/',views.StreamQuiz_result,name='stream-result'),
path('result/',views.CareerQuiz_result ,name='result')
#path('chart/',views.getimage,name='charts')
] 



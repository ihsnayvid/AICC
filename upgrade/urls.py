from django.urls import path
from . import views

urlpatterns = [
path('advance_result/',views.predicts, name='aresult'),
path('advance_test/',views.advance_Quiz,name='advance_test'),
path('premium',views.premium_intro,name='upgrade'),
path('choose_your_career/',views.choose_career,name='choose')
]
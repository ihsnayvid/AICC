from django.urls import path
from . import views

urlpatterns=[
path('feedback/',views.review,name='feedbacks')
]

from django.urls import path
from .import views
urlpatterns = [
path('college/',views.searchclg,name='clg')
]
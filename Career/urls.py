from django.urls import path
from .import views

urlpatterns = [
path('careerlibrary/',views.careerlib, name='careerlibrary'),
path('law/',views.law_career,name='law'),
path('architecture/',views.architecture_career,name='architecture'),
path('pilot/',views.pilot_career,name='pilot'),
path('medicine/',views.medicine_career,name='medicine'),
path('fashion/',views.fashion_career,name='fashion'),
path('civil_services/',views.civil_career,name='civil'),
path('management/',views.manage_career,name='manage'),
path('defense/',views.defense_career,name='defense'),
path('computer/',views.computer_career,name='computer'),
path('cabin_crew/',views.cabin_career,name='cabin'),
path('food_technology/',views.food_career,name='food'),
path('banking/',views.bank_career,name='bank'),
path('education/',views.education_career,name='education'),
path('commerce/',views.commerce_career,name='commerce'),
path('arts/',views.arts_career,name='arts'),
path('career-search/',views.searchcareer,name='career-search')
]

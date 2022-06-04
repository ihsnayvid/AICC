from django.urls import path
from users import views as user_views
from index import views as index_views


urlpatterns = [
path('',index_views.homepage,name='homepage'),
path('stream-planning/',index_views.classeight,name='8-9'),
path('career-planning/',index_views.classeleven,name='10-12')

]
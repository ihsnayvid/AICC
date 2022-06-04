"""AICC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from Quiz import views as quiz_views
#from django_otp.admin import OTPAdminSiteadmin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('profile/',user_views.profile,name='profile'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
   # path('userform2/',user_views.user2form_add ,name='form2'),
    path('userform3/',user_views.user3form_add ,name='form3'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('',include('blog.urls')),
    path('',include('Quiz.urls')),
    path('',include('index.urls')),
    path('',include('Career.urls')),
    path('',include('College.urls')),
    path('',include('Review_mgmt.urls')),
    path('login/',user_views.login,name='login'), 
    path('logout/',user_views.logout,name='logout'),
    path('',include('chatbot.urls')),
    path('',include('upgrade.urls'))
    ]
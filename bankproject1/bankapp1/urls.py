from django.urls import path
from . import  views
app_name='bankapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('register',views.register,name='register'),
    path('form', views.form, name='form'),
    path('login', views.login, name='login'),
    path('user', views.user, name='user'),


]
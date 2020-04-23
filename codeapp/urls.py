from django.urls import path
from .views import *

urlpatterns = [
	path('',index,name='index'),
	path('register',register, name='register'),
	path('dashboard',dashboard, name='dashboard'),
	path('rankboard',rankboard, name='rankboard'),
	path('contest',contest, name='contest'),
	path('alinks',alinks, name='alinks'),


]
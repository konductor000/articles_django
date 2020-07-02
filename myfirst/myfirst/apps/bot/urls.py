from django.urls import path
from . import views

app_name = 'bot'

urlpatterns = [
	path('', views.bot, name='bot'),
	path('Eat/', views.Eat, name = 'Eat'),
	path('GoToTheHospital/', views.GoToTheHospital, name = 'GoToTheHospital'),
	path('GoToTheShop/', views.GoToTheShop, name = 'GoToTheShop'),
	path('GoToTheWork/', views.GoToTheWork, name = 'GoToTheWork'),
	path('Sleep/', views.Sleep, name = 'Sleep'),
	path('ReturnAll/', views.ReturnAll, name = 'ReturnAll'),
]
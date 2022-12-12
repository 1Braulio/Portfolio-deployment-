from . import views
from django.urls import path

app_name = 'user'
urlpatterns = [
	path('login', views.loginPage, name = 'login'),
	path('logout', views.logoutUser, name = 'logout'),
	path('register', views.registrationPage, name = 'register'),
	path('home', views.home, name = 'home'),
]
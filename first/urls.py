from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns=[
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('login/',LoginView.as_view(),name='login_url'),
	path('register/', views.register, name='register_url'),
	path('logout/',LogoutView.as_view(),name='logout'),


]

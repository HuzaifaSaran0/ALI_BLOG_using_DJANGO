from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
    path('', views.home, name='home'),
    # path('contact/', views.contact, name='contact'),
    # path('about/', views.about, name='about'),
]

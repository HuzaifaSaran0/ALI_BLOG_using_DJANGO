# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('bloghome/', views.bloghome, name='bloghome'),
    # path('', views.bloghome, name='home'),
    path('', views.bloghome, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('postComment/', views.postComment, name='postComment'),
    # path('blogpost/', views.blogpost, name='blogpost'),
    path('<str:slug>/', views.blogpost, name='home'),
]

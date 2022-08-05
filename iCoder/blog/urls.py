from django import views
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('iCoder/', views.iCoder, name='iCoder'),
    path('blogpost/<int:slug>', views.blogpost, name='blogpost'),
    path('search/', views.search, name='search'),
    path('signup/', views.handleSignup, name='handleSignup'),
    path('login/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),


]
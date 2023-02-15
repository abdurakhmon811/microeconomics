"""Defines URLPATTERNS for the 'main' application."""
from django.urls import path
from . import views

appname = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<str:blog_title>/', views.blog, name='blog'),
    path('files/', views.files, name='files'),
    path('search/', views.search, name='search'),
]
"""Defines URLPATTERNS for the 'main' application."""
from django.urls import path
from . import views

appname = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<str:blog_title>/', views.blog, name='blog'),
    path('blogs/new-post/publish/', views.publish_blog, name='publish_blog'),
    path('blogs/delete/<str:blog_title>/', views.delete_blog, name='delete_blog'),
    path('files/', views.files, name='files'),
    path('files/add/', views.add_file, name='add_file'),
    path('files/delete/<str:file_name>/', views.delete_file, name='delete_file'),
    path('search/', views.search, name='search'),
    path('ramazonov-shamil-login/', views.ramazonov_shamil_login, name='ramazonov_shamil_login'),
    path('logout-superuser/', views.logout_superuser, name='logout_superuser'),
]
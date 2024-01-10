from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
     path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about')
]
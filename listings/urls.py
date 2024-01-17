from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id', views.listing, name='listing'),
    path('search', views.search, name='search'),
    # path('index.html', views.index, name='index'),
    # path('about.html', views.about, name='about')
]

from django.urls import path
from . import views

# app_name
app_name = 'home'

# urls
urlpatterns = [
    path('', views.index, name='index'),
    path('components/', views.components, name='components'),
    path('favourites/', views.favourites, name='favourites'),
]
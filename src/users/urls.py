from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
    path('signup/', views.register, name='register'),
    path('signout/', views.user_logout, name='signout'),
]
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# app_name
app_name = 'home'

# urls
urlpatterns = [
    path('', views.index, name='index'),
    path('components/', views.components, name='components'),
    path('components/charts/', views.charts, name='tables'),
    path('components/tables/', views.tables, name='charts'),
    path('favourites/', views.favourites, name='favourites'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
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
    path('components/charts/', views.charts_select, name='charts'),
    path('components/charts/', views.charts, name='charts_results'),
    path('components/tables/', views.tables, name='tables'),
    path('components/tables/results/', views.table_result, name='table_results'),
    path('my_files/', views.my_files, name='favourites'),
    path('redirect/', views.my_files, name='favourites'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
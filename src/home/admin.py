from django.contrib import admin
from .models import TableDataFile, ChartDataFile

# Register your models here.
admin.site.register(TableDataFile)
admin.ste.register(ChartDataFile)
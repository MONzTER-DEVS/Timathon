from django.contrib import admin
from .models import TableDataFile, ChartDataFile, UserFile

# Register your models here.
admin.site.register(TableDataFile)
admin.site.register(ChartDataFile)
admin.site.register(UserFile)

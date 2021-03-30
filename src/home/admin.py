from django.contrib import admin
from .models import TableDataFile, ChartDataFile, UserFile
from .forms import *
# Register your models here.
admin.site.register(TableDataFile)
admin.site.register(ChartDataFile)
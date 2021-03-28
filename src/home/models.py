from django.db import models


# Create your models here.
class TableDataFile(models.Model):
    file = models.FileField(blank=True)


class ChartDataFile(models.Model):
    chart_file = models.FileField(blank=True)


class UserFile(models.Model):
    user_name = models.CharField(max_length=151)
    file_name = models.CharField(max_length=200)
    original_file_name = models.CharField(max_length=200)

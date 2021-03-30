from django.db import models
from django.forms import ModelForm


# Create your models here.
class TableDataFile(models.Model):
    file = models.FileField(blank=True)


class ChartDataFile(models.Model):
    chartfile = models.FileField(blank=True)


class UserFile(models.Model):
    username = models.CharField(max_length=151)
    file = models.FileField(null=True)
    original_file_name = models.CharField(max_length=200)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

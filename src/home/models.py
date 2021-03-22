from django.db import models


# Create your models here.
class TableDataFile(models.Model):
    file = models.FileField(blank=True)


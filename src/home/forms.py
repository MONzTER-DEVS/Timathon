from .models import TableDataFile
from django import forms


class TableDataForm(forms.ModelForm):
    class Meta:
        model = TableDataFile
        fields = ('file',)

from .models import TableDataFile
from django import forms


class TableDataForm(forms.ModelForm):
    class Meta:
        model = TableDataFile
        fields = ('file',)

    def __init__(self, *args, **kwargs):
        super(TableDataForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs = {
            'class': 'file-upload-btn',
            'id': 'file-upload'
        }
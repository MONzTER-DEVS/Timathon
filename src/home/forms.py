from .models import TableDataFile, ChartDataFile, UserFile
from django import forms


class TableDataForm(forms.ModelForm):
    class Meta:
        model = TableDataFile
        fields = ('file',)

    def __init__(self, *args, **kwargs):
        super(TableDataForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs = {
            'class': 'file-upload-btn',
            'id': 'file-upload-id'
        }


class ChartDataForm(forms.ModelForm):
    class Meta:
        model = ChartDataFile
        fields = ('chartfile',)

    def __init__(self, *args, **kwargs):
        super(ChartDataForm, self).__init__(*args, **kwargs)
        self.fields['chartfile'].widget.attrs = {
            'class': 'file-upload-btn-chart',
            'id': 'file-upload-id-chart'
        }


class UploadedFilesForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['username', 'file', 'original_file_name']

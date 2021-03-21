from django import forms


class UploadDataFile(forms.Form):
    file = forms.FileField()


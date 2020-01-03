from django import forms
# from cal.models import RScript


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
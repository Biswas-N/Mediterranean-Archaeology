from .models import RecordImage
from django import forms

class RecordImageForm(forms.ModelForm):
    class Meta:
        model = RecordImage
        fields = ('image', 'record')
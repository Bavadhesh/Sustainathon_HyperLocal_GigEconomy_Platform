from django import forms
from .models import RequestBox

class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestBox
        fields = "__all__"
        exclude = ['user','accepted']
        
        # Add more fields as needed
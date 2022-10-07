from django import forms
from .models import Phone

class create_form(forms.Form):

    name=forms.CharField()
    
    
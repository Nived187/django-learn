from django import forms


class RawInput(forms.Form):

    title = forms.CharField()
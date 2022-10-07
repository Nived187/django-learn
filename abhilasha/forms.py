from django import forms

class ComplaintsF(forms.Form):

    title = forms.CharField(label="",
                    widget=forms.TextInput(
                            attrs = {
                                "placeholder":"enter"
                            }
                        )
                        )
    description = forms.CharField()

from django import forms


class CarForm(forms.Form):

    name = forms.CharField(label="Car name : ",
                            widget=forms.TextInput(
                                attrs = {
                                    "placeholder":"enter value"
                                    }
                                )

                        )
    price = forms.CharField()
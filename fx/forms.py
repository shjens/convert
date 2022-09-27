from django import forms


class FormAmount(forms.Form):
    amount = forms.IntegerField()
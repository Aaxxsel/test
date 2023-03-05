from django import forms


class TitleText(forms.Form):
    title = forms.CharField()
    text = forms.CharField()

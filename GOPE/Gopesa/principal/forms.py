from django import forms


class FormName(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField();
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

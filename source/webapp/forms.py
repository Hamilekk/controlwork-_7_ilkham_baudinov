from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


class GuestForms(forms.Form):
    name = forms.CharField(required=True, max_length=100, label='Имя гостя')
    email = forms.EmailField(required=True, max_length=200, label='Почта гостя')
    text = forms.CharField(max_length=3000, required=True, label='Описание', widget=widgets.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError('Имя не может быть короче двух символов')
        return name

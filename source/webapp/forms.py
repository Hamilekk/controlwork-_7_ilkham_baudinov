from django import forms
from django.forms import widgets


class GuestForms(forms.Form):
    name = forms.CharField(required=True, max_length=100, label='Имя гостя')
    email = forms.EmailField(required=True, max_length=200, label='Почта гостя')
    text = forms.CharField(max_length=3000,required=True, label='Описание', widget=widgets.Textarea)
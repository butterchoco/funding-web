from django import forms
from .models import testi_Model

class testi_form(forms.Form):
    name = forms.CharField(max_length=200,widget=forms.HiddenInput())
    komenAttrs={'class': 'form-control', 'placeholder': 'Sampaikan pengalaman anda...', 'type':'text', 'rows':'5'}
    komentar = forms.CharField(max_length=1000,widget=forms.Textarea(attrs=komenAttrs))

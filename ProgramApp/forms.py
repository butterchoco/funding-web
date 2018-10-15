from django import forms
from django.forms import ModelForm


class program_registration_form(ModelForm):
    tanggal_lahir = forms.DateField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}), input_formats=['%d-%m-%Y'])
    
    class Meta:
        field = ['nama', 'tanggal_lahir', 'jumlah_uang']
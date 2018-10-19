from django import forms
from .models import program_update


class MyModelChoiceField(forms.ModelChoiceField):
    widget = forms.Select(attrs={'class': 'form-control'})
    empty_label = "Pilih program donasi"

    def label_from_instance(self, obj):
        return obj.judul


class program_registration_form(forms.Form):
    program = MyModelChoiceField(program_update.objects.all())
    nama = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control shadow-box-form', 'placeholder': 'Isi nama kamu di sini...'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control shadow-box-form', 'placeholder': 'Isi email kamu di sini...'}))
    jumlah_uang = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control shadow-box-form', 'placeholder': 'Masukkan jumlah uang !'}))
    tampilkan = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput())
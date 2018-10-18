from django import forms


class program_registration_form(forms.Form):
    nama = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control shadow-box-form', 'placeholder': 'Isi nama kamu di sini...'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control shadow-box-form', 'placeholder': 'Isi email kamu di sini...'}))
    jumlah_uang = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control shadow-box-form', 'placeholder': 'Masukkan jumlah uang !'}))
    tampilkan = forms.BooleanField(widget=forms.CheckboxInput())
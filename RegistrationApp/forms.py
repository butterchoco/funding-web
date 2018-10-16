from django import forms


class user_registration_form(forms.Form):
    nama = forms.CharField(max_length=255)
    tanggal_lahir = forms.DateField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}), input_formats=['%Y-%m-%d'])
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
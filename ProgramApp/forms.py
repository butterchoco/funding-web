from django import forms


class program_registration_form(forms.Form):
    nama = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField()
    jumlah_uang = forms.IntegerField()
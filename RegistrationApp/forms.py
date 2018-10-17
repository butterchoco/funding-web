from django import forms
from .models import user_registration

class tanggalWidget(forms.DateInput):
    input_type = 'date'

class passwordWidget(forms.PasswordInput):
    input_type = 'password'

class user_registration_form(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(user_registration_form, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = user_registration
        fields = [
            'nama',
            'tanggal_lahir',
            'email',
            'password',
        ]
        widgets = {
            'tanggal_lahir' : tanggalWidget(),
            'password' : passwordWidget(),
        }
    # nama = forms.CharField(max_length=255)
    # tanggal_lahir = forms.DateField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}), input_formats=['%Y-%m-%d'])
    # email = forms.EmailField()
    # password = forms.CharField(max_length=50, widget=forms.PasswordInput())

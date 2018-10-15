from django.shortcuts import render
from .forms import program_registration_form
from .models import program_registration
from django.http import HttpResponseRedirect

response = {}


def programIndex(request):
    if (request.method == "POST"):
        form = program_registration_form(request.POST)
        if (form.is_valid()):
            response['nama'] = request.POST['nama']
            response['email'] = request.POST['email']
            response['jumlah_uang'] = request.POST['jumlah_uang']
            forms = program_registration(nama=response['nama'], email=response['email'], jumlah_uang=response['jumlah_uang'])
            forms.save()
            return HttpResponseRedirect('/program/')
    else:
        form = program_registration_form()
    return render(request, 'index.html', {'form': form})
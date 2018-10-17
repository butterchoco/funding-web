from django.shortcuts import render, get_object_or_404
from .forms import program_registration_form
from .models import program_registration, program_update
from django.http import HttpResponseRedirect
response = {}


def programIndex(request):
    program = program_update.objects.all()
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
    return render(request, 'program_index.html', {'form': form, 'program': program})


def programUpdate(request, id=None):
    program = get_object_or_404(program_update, id=id)
    program_reg = program_registration.objects.all()
    return render(request, 'programUpdate.html', {'program': program, 'program_reg': program_reg})

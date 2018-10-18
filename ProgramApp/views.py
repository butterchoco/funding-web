from django.shortcuts import render, get_object_or_404
from .forms import program_registration_form
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from RegistrationApp.models import user_registration
from .models import program_registration, program_update
from django.http import HttpResponseRedirect
response = {}


def programIndex(request):
    program = program_update.objects.all()
    if (request.method == "POST"):
        form = program_registration_form(request.POST)
        if (form.is_valid()):
            try:
                test = user_registration.objects.get(email=request.POST['email'])
            except ObjectDoesNotExist:
                messages.error(request, "Email belom terdaftar")
                return HttpResponseRedirect('/program/')
            response['nama'] = request.POST['nama']
            response['email'] = request.POST['email']
            response['jumlah_uang'] = request.POST['jumlah_uang']
            response['tampilkan'] = request.POST['tampilkan']
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

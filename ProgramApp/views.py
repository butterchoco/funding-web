from django.shortcuts import render, get_object_or_404
from .forms import program_registration_form
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from RegistrationApp.models import user_registration
from .models import program_registration, program_update
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
response = {}


def programIndex(request):

    # membuat session setelah user login
    if request.user.is_authenticated:
        strNama = request.user.first_name + " " + request.user.last_name
        strNama = strNama.strip()
        request.session['name'] = strNama
        request.session['email'] = request.user.email
        response['nama'] = request.session['name']
    

    if (request.method == "POST"):
        form = program_registration_form(request.POST)
        response['form'] = form
        if (form.is_valid()):
            response['jumlah_uang'] = request.POST['jumlah_uang']
            response['tampilkan'] = form.cleaned_data['tampilkan']
            response['program'] = form.cleaned_data['program']
            forms = program_registration(program=response['program'], nama=request.session['name'], email=request.session['email'], jumlah_uang=response['jumlah_uang'], tampilkan=response['tampilkan'])
            forms.save()
            return HttpResponseRedirect('/program/')
    else:
        response['form']= program_registration_form()

    program = program_update.objects.all()
    response['program'] = program
    return render(request, 'program_index.html', response)


def programUpdate(request, id=None):
    if request.user.is_authenticated:
        strNama = request.user.first_name + " " + request.user.last_name
        strNama = strNama.strip()
        request.session['name'] = strNama
        request.session['email'] = request.user.email
        response['nama'] = request.session['name']
    program = get_object_or_404(program_update, id=id)
    program_reg = program_update.objects.get(id=id).program_registration_set.all()
    totalDonasi = 0
    for temp in program_reg:
        totalDonasi += temp.jumlah_uang

    response['program'] = program
    response['program_reg'] = program_reg
    response['totalDonasi'] = totalDonasi
    return render(request, 'programUpdate.html', response)

def validate(request):
    if (request.method == "POST"):
        email = request.POST['email']
        nama = request.POST['nama']
        check = False
        check2 = False
        for i in user_registration.objects.filter(nama=nama):
            if (i.nama == nama):
                check2 = True
                break
        for i in user_registration.objects.filter(email=email):
            if (i.email == email):
                check = True
                break
        data = {
            'is_taken': check,
            'nama_is_taken': check2
        }
        return JsonResponse(data)
    return HttpResponse('OK')
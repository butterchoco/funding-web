from django.shortcuts import render
from django.contrib import messages
from .forms import user_registration_form
from .models import user_registration
from django.http import HttpResponseRedirect
# Create your views here.
response = {}


def registrationIndex(request):
    if (request.method == "POST"):
        user_form = user_registration_form(request.POST)
        if (user_form.is_valid()):
            response['nama'] = request.POST['nama']
            response['tanggal_lahir'] = request.POST['tanggal_lahir']
            if (user_registration.objects.filter(email=user_form.cleaned_data['email']).exists()):
                messages.error(request, "This email has already existed.")
                return HttpResponseRedirect('/registration/')
            response['email'] = request.POST['email']
            response['password'] = request.POST['password']
            form = user_registration(nama=response['nama'], tanggal_lahir=response['tanggal_lahir'], email=response['email'], password=response['password'])
            form.save()
            return HttpResponseRedirect('/program/')
    else:
        user_form = user_registration_form()
    return render(request, 'registration_index.html', {'user_form': user_form})

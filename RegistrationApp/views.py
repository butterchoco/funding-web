from django.shortcuts import render
from django.contrib import messages
from .forms import user_registration_form, login_form
from .models import user_registration
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
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
            user = User.objects.create_superuser(response['nama'], response['email'], response['password'])
            name = response['nama'].split(' ')
            user.first_name = name[0]
            user.last_name = ""
            user.save()
            form.save()
            return HttpResponseRedirect('/program/')
    else:
        user_form = user_registration_form()
    return render(request, 'registration_index.html', {'user_form': user_form})

def loginIndex(request):
    if (request.method == "POST"):
        form = login_form(request.POST)
        if (form.is_valid()):
            response['nama'] = request.POST.get('nama', False)
            response['password'] = request.POST.get('password', False)
            print(response['nama'], response['password'])
            users = authenticate(request, username=response['nama'], password=response['password'])
            if users is not None:
                if users.is_active:
                    login(request, users)
                    return HttpResponseRedirect('/program/')
                else:
                    messages.error(request, "Login Failed.")
            else:
                messages.error(request, "Invalid Username or Password")
            print('masuk2')
    else:
        form = login_form()
    return render(request, 'login_index.html', {'form': form})

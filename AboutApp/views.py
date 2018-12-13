from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import testi_form
from .models import testi_Model

# Create your views here.
response = {}

def aboutIndex(request):
    allTesti = testi_Model.objects.all()
    if request.user.is_authenticated:
        strNama = request.user.first_name + " " + request.user.last_name
        strNama = strNama.strip()
        request.session['name'] = strNama
        request.session['email'] = request.user.email
    if (request.method == "POST"):
        form = testi_form(request.POST)
    else:
        form = testi_form()
        
    if 'name' in request.session:
        form = testi_form(initial={'name':request.session['name']})
        response['nama'] = request.session['name']
    else:
        response['nama'] = ''
    return render(request, 'about.html', {'form':form, 'allTesti':allTesti, 'nama':response['nama']})

def tambah_komentar(request):
    if request.user.is_authenticated:
        nama = request.user.first_name + " " + request.user.last_name
        nama = nama.strip()
    
    print(request.user.is_authenticated)
    if (request.method == "POST"):
        name = nama
        komentar = request.POST.get('komentar', False)
        testi = testi_Model(name = name, komenModel = komentar)
        testi.save()
    return HttpResponse("OK")
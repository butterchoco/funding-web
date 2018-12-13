<<<<<<< HEAD
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import testi_form
from .models import testi_Model

# Create your views here.

def aboutIndex(request):
    allTesti = testi_Model.objects.all()
    if request.user.is_authenticated:
        strNama = request.user.first_name + " " + request.user.last_name
        strNama = strNama.strip()
        request.session['name'] = strNama
        request.session['email'] = request.user.email
    if (request.method == "POST"):
        form = testi_form(request.POST)
        if (form.is_valid()):
            name = request.POST['name']
            komentar = request.POST['komentar']
            testi = testi_Model(name = name, komenModel = komentar)
            testi.save()
            return redirect('/testi_json')
    form = testi_form()
    if 'name' in request.session:
        form = testi_form(initial={'name':request.session['name']})
        nama = request.session['name']
    else:
        nama = ''
    return render(request, 'about.html', {'form':form, 'allTesti':allTesti, 'nama':nama})

def testi_json(request):
    testiDict = [obj.as_dict() for obj in testi_Model.objects.all()]
    return JsonResponse({"testimonies": testiDict}, content_type='application/json')

=======
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
>>>>>>> f4a7cff61f49d7c2f3a284dcdcccc966e9f9bd86

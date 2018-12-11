from django.shortcuts import render
from django.http import HttpResponseRedirect
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
            return HttpResponseRedirect('/about/')
    form = testi_form()
    if 'name' in request.session:
        form = testi_form(initial={'name':request.session['name']})
        nama = request.session['name']
    else:
        nama = ''
    return render(request, 'about.html', {'form':form, 'allTesti':allTesti, 'nama':nama})

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import testi_form
from .models import testi_Model

# Create your views here.

def aboutIndex(request):
    allTesti = testi_Model.objects.all()
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
    return render(request, 'about.html', {'form':form, 'allTesti':allTesti})

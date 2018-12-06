from django.shortcuts import render
from .forms import testi_form
from .models import testi_Model

# Create your views here.

def aboutIndex(request):
    if (request.method == "POST"):
        form = testi_form(request.POST)
        if (form.is_valid()):
            name = request.POST['name']
            komentar = request.POST['komentar']
            testi = testi_Model(name = name, komentar = komentar)
            testi.save()
            return redirect('/about/')
    else:
        form = testi_form()
        if 'name' in request.session:
            form = testi_form(initial={'name':request.session['name']})
    return render(request, 'about.html', {'form':form})

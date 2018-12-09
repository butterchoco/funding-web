from django.shortcuts import render, get_object_or_404
from .models import news_update
# Create your views here.


def newsIndex(request):
    berita = news_update.objects.all()
    if request.user.is_authenticated:
        strNama = request.user.first_name + " " + request.user.last_name
        strNama = strNama.strip()
        request.session['name'] = strNama
        request.session['email'] = request.user.email
    if 'name' in request.session:
        nama = request.session['name']
    else:
        nama = ''
    return render(request, 'news_index.html', {'berita': berita, 'nama':nama})


def newsDetails(request, id=None):
    berita = get_object_or_404(news_update, id=id)
    return render(request, 'newsDetails.html', {'berita': berita})
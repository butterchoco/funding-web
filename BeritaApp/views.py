from django.shortcuts import render
from .models import news_update
# Create your views here.


def newsIndex(request):
    berita = news_update.objects.all()
    return render(request, 'news_index.html', {'berita': berita})
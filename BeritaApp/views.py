from django.shortcuts import render, get_object_or_404
from .models import news_update
# Create your views here.


def newsIndex(request):
    berita = news_update.objects.all()
    return render(request, 'news_index.html', {'berita': berita})


def newsDetails(request, id=None):
    berita = get_object_or_404(news_update, id=id)
    return render(request, 'newsDetails.html', {'berita': berita})
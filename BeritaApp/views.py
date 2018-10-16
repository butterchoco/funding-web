from django.shortcuts import render

# Create your views here.


def newsIndex(request):
    return render(request, 'news_index.html')
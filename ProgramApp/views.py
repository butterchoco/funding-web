from django.shortcuts import render


def programIndex(request):
    return render(request, 'index.html')
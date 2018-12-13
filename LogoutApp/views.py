from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout as logout_fun

def logout(request):
    logout_fun(request)
    return redirect('/program')

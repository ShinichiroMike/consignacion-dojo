from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html', {'greeting': 'hello'})
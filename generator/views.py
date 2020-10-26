from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/index.html')

def sPass(request):

    generatedPass = ""

    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get('uppercase'):
        characters.extend(list("ABCDEFGHIJKLMNOPQURSTUVWXYZ"))

    if request.GET.get('special'):
        characters.extend(list(" !@#$%^&*() "))

    if request.GET.get('Numbers'):
        characters.extend(list("0123456789"))

    length = int(request.GET.get("length"))

    for x in range(length):
        generatedPass += random.choice(characters)
    return render(request,'generator/showPass.html',{'password':generatedPass})

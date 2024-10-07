from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from . models import generator

def gerador(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    
    if request.method == 'POST':
        char_range = request.POST.get('char_range')

        password = ''.join(generator(char_range))
        if password:
            return render(request, 'index.html', {'password':password})

        return redirect(gerador)
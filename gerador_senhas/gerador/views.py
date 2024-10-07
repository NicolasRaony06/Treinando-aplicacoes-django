from django.shortcuts import render
from django.http import HttpResponse

def gerador(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    
    if request.method == 'POST':
        pass
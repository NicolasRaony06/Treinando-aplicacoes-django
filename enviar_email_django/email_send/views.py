from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def send_email(request, email):
    if request.method == 'GET':
        print(type(email))
        send_mail('Teste de Envio', 'Este é um email de teste', '___', [email]) #TODO add email
        return HttpResponse('Email Enviado!')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Token, token_is_valid
import random
from django.core.mail import send_mail

def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'cadastrar.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        return HttpResponse("Cadastrado!")
    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            return HttpResponse('Logado!')
        
        return HttpResponse('Erro!')
    
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponse('Deslogado!')
    
def reset_password(request):
    if request.method == 'GET':
        return render(request, 'reset_password.html')
    if request.method == 'POST':
        user_email = request.POST.get('user_email')

        user = User.objects.filter(email=user_email)

        if user:
            email_token_code = random.randint(1000, 9999)
            url_token_code = random.randint(1000, 9999)

            token = Token(
                user = User.objects.get(email=user_email),
                email_token_code = email_token_code,
                url_token_code = url_token_code,
            )

            token.save()

            send_mail("Código para Resetar Senha", f"O seu código para resetar sua senha é {email_token_code}.", "nrdq59443@gmail.com", [f'{user_email}'])

            return redirect(f'/users/receive_token/{user_email}')

def receive_token(request, user_email):
    if request.method == 'GET':
        return render(request, 'receive_token.html', {'user_email': user_email})
    if request.method == 'POST':
        email_token_code = request.POST.get('email_token_code')
        user = User.objects.filter(email=user_email)

        if user:
            user = User.objects.get(email=user_email)
            
            tokens = Token.objects.filter(user=user).filter(email_token_code=email_token_code).filter(used=False)

            if tokens:
                token = Token.objects.get(user=user, email_token_code=email_token_code)

                if not token_is_valid(token):
                    print(token_is_valid(token))
                    return HttpResponse('Token expirado!')

                url_token_code = token.url_token_code

                return redirect(f'/users/change_password/{user_email}/?url_token_code={url_token_code}')
            
            return HttpResponse('Token Não existe!')
        
        return HttpResponse("Não existe usuário com esse email!")

def change_password(request, user_email):
    if request.method == 'GET':
        url_token_code = request.GET.get('url_token_code')

        user = User.objects.filter(email=user_email)

        if user:
            user = User.objects.get(email=user_email)
            
            tokens = Token.objects.filter(user=user).filter(url_token_code=url_token_code).filter(used=False)

            if tokens:
                token = Token.objects.get(user=user, url_token_code=url_token_code, used=False)

                if not token_is_valid(token):
                    print(token_is_valid(token))
                    return HttpResponse('Token expirado!')

                token.used = True

                token.save()

                return render(request, 'change_password.html', {'user_email': user_email})
            
            return HttpResponse('Token inválido!')

        return HttpResponse('Email de usuário inválido!')
    
    if request.method == 'POST':
        new_password = request.POST.get('new_password')

        user = User.objects.get(email=user_email)

        user.set_password(new_password)

        user.save() 

        return HttpResponse("Senha alterada!")


        

        
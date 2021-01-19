from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
from django.http import JsonResponse

# Create your views here.
# def index(request):
#     return render(request, 'login/index.html')


def login(request):
    if request.session.has_key('password'):
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'faiz' and password == '1234':
            request.session['password'] = password
            return JsonResponse('true', safe=False)

        else:
            return JsonResponse('false', safe=False)
    else:
        return render(request, 'login/index.html')


def home(request):
    if request.session.has_key('password'):
        return render(request, 'login/home.html')
    else:
        return redirect(login)


def logout(request):
    if request.session.has_key('password'):
        request.session.flush()
        return redirect(login)
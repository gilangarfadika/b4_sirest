# from django.shortcuts import render

# from urllib import request

# from django.shortcuts import redirect

# from django.contrib import messages

# from django.contrib import auth

# from django.contrib.auth.decorators import login_required

# import datetime

# from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
# from django.urls import reverse

# from django.core import serializers

# from django.utils.decorators import method_decorator



# def show_register(request):
#     current_user = auth.get_user(request)


#     # if(not current_user.is_admin):
#     #     return redirect('authentication:login')

#     context = {}
#     return render(request, "register.html", context)

# def show_register_restoran(request):
#     return render(request, "register_restoran.html")


# def show_register_kurir(request):
#     current_user = auth.get_user(request)


#     # if(not current_user.is_admin):
#     #     return redirect('authentication:login')

#     context = {}
#     return render(request, "register_kurir.html", context)

# def show_register_admin(request):
#     return render(request, "register_admin.html")

# def show_register_pelanggan(request):
#     return render(request, "register_pelanggan.html")


# def show_login_register(request):
#     return render(request, 'Login&Register.html')

# def show_login(request):
#     return render(request, 'login.html')
from django.shortcuts import render, redirect
from .models import UserAccRepository
from django.http import HttpResponse

# def login_ta(request):

#     if request.method == "POST":

#         email = request.POST["email"]
#         password = request.POST["password"]
#         uar = UserAccRepository()
#         ua = uar.getByEmailPassword(email, password)
    
#     return HttpResponse(f"{email},{password}")

def login_ta(request):

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]
        uar = UserAccRepository()
        user_exist = uar.isUserExist(email, password)

        if user_exist:
            request.session['user_email'] = email
            request.session['user_password'] = password
            return redirect('/authentication/login-after/')
        else:
            return show_login(request, user_not_exist=True)

def afterlogin(request):
    uar = UserAccRepository()
    user = uar.getByEmailPassword(request.session.get('user_email'), request.session.get('user_password'))
    print(user)
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    return render(request, 'test_page.html', {"user": user})

def show_login(request, user_not_exist = False):
    return render(request, 'login.html', {"user_not_exist": user_not_exist})

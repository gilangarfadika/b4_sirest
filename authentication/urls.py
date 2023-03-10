from django.urls import path

from .views import *

app_name = 'authentication'

urlpatterns = [
    # path("register/", show_register, name="show_register"),
    # path("register-admin/", show_register_admin, name="show_register_admin"),
    # path("register-pelanggan/", show_register_pelanggan, name="show_register_pelanggan"),
    # path("login_register/", show_login_register, name="show_login_register"),
    path('', index, name="index"),
    path("login/", show_login, name="show_login"),
    path("register-all/", register_all, name="show_register_all"),
    path('login-request/', login_ua, name='login_request'),
    path("login-after/", afterlogin, name="logintest"),
    path("logged_admin/", after_login_admin, name="logged_admin"),
    path("logged_customer/", after_login_customer, name="logged_customer"),
    path("logged_restaurant/", after_login_restaurant, name="logged_restaurant"),
    path("logout/", logout, name="testlogout"),
    path("register-restoran/", show_register_restoran, name="show_register_restoran"),
    path("register-restoran-logic/", register_restoran, name="register_restoran"),
    path("register-kurir/", show_register_kurir, name="show_register_kurir"),
    path("register-kurir-logic/", register_kurir, name="register_kurir"),
]
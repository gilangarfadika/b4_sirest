"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('restopay/', include('restopay.urls')),
    path('jam_operasional/', include('jam_operasional.urls')),
     path('transaksi_pesanan/', include('transaksi_pesanan.urls')),
    path('kategori_makanan/', include('kategori_makanan.urls')),
    path('tarifPengiriman/', include('tarifPengiriman.urls')),
    path('Makanan/', include('Makanan.urls')),
    path('authentication/', include('authentication.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('kategori_restoran/', include('kategori_restoran.urls')),
    path('bahan_makanan/', include('bahan_makanan.urls')),
    path('Riwayat/', include('Riwayat.urls')),
    path('Promo/', include('Promo.urls')),
    path('PromoRestoran/', include('PromoRestoran.urls')),
]

urlpatterns += staticfiles_urlpatterns()
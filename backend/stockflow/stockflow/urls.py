from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'api/',
        include('inventaire.urls')
    ),

    path(
        'api/',
        include('commandes.urls')
    ),

    path(
        'api/',
        include('dashboard.urls')
    ),
    path(
    'api/',
    include('statistiques.urls')
),
]
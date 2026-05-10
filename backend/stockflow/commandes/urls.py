from django.urls import path
from .views import *

urlpatterns = [

    path(
        'commandes',
        commandes
    ),

    path(
        'commandes/<int:id>',
        commande_detail
    ),

    path(
        'commandes/<int:id>/statut',
        changer_statut
    ),
]
from django.urls import path
from .views import *

urlpatterns = [

    path('produits', produits),

    path('produits/<int:id>', produit_detail),

    path(
        'produits/<int:id>/stock',
        modifier_stock
    ),
]
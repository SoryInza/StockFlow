from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response

from inventaire.models import Produit
from commandes.models import Commande


@api_view(['GET'])
def statistiques(request):

    boutique_id = request.GET.get(
        'boutique_id'
    )

    produits = Produit.objects.filter(
        boutique_id=boutique_id
    )

    commandes = Commande.objects.filter(
        boutique_id=boutique_id
    )

    total_stock = 0
    total_valeur = 0

    categories = {}

    for produit in produits:

        total_stock += produit.quantite_stock

        total_valeur += (
            produit.quantite_stock *
            produit.prix_unitaire
        )

        categorie = produit.categorie

        if categorie not in categories:

            categories[categorie] = 0

        categories[categorie] += 1

    produits_alertes = 0

    for produit in produits:

        if produit.en_alerte:

            produits_alertes += 1

    commandes_livrees = commandes.filter(
        statut='livree'
    ).count()

    commandes_attente = commandes.filter(
        statut='en_attente'
    ).count()

    data = {

        "stock": {

            "total_stock": total_stock,

            "valeur_totale": total_valeur,

            "produits_alertes": produits_alertes
        },

        "commandes": {

            "livrees": commandes_livrees,

            "en_attente": commandes_attente
        },

        "categories": categories
    }

    return Response(data)
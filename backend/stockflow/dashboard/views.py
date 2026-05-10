from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response

from inventaire.models import Produit
from commandes.models import Commande

@api_view(['GET'])
def dashboard(request):

    boutique_id = request.GET.get(
        'boutique_id'
    )

    if not boutique_id:

        return Response(
            {
                "message":
                "boutique_id requis"
            },
            status=400
        )

    produits = Produit.objects.filter(
        boutique_id=boutique_id
    )

    total_produits = produits.count()

    produits_ok = 0
    produits_en_alerte = 0
    produits_en_rupture = 0

    valeur_totale_stock = 0

    alertes = []

    for produit in produits:

        valeur_totale_stock += (
            produit.quantite_stock *
            produit.prix_unitaire
        )

        if produit.quantite_stock == 0:

            produits_en_rupture += 1

        elif produit.en_alerte:

            produits_en_alerte += 1

        else:

            produits_ok += 1

        if produit.en_alerte:

            deficit = (
                produit.quantite_stock -
                produit.seuil_alerte
            )

            alertes.append({

                "id": produit.id,

                "nom": produit.nom,

                "stock":
                produit.quantite_stock,

                "seuil":
                produit.seuil_alerte,

                "deficit":
                deficit
            })

    alertes = sorted(
        alertes,
        key=lambda x: x['deficit']
    )

    alertes_critiques = alertes[:5]

    commandes = Commande.objects.filter(
        boutique_id=boutique_id
    )

    commandes_en_attente = commandes.filter(
        statut='en_attente'
    )

    aujourd_hui = timezone.now().date()

    commandes_en_retard = commandes.filter(
        date_livraison_prevue__lt=aujourd_hui
    ).exclude(
        statut__in=['livree', 'annulee']
    )

    commandes_recentes = commandes.order_by(
        '-date_creation'
    )[:3]

    recentes = []

    for commande in commandes_recentes:

        recentes.append({

            "id": commande.id,

            "fournisseur":
            commande.fournisseur_nom,

            "statut":
            commande.statut,

            "date":
            commande.date_creation
        })

    data = {

        "resume": {

            "total_produits":
            total_produits,

            "produits_ok":
            produits_ok,

            "produits_en_alerte":
            produits_en_alerte,

            "produits_en_rupture":
            produits_en_rupture,

            "valeur_totale_stock":
            valeur_totale_stock
        },

        "alertes_critiques":
        alertes_critiques,

        "commandes_en_attente": {

            "total":
            commandes_en_attente.count(),

            "en_retard":
            commandes_en_retard.count()
        },

        "commandes_recentes":
        recentes
    }

    return Response(data)
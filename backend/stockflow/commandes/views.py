from django.db import transaction
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Commande
from .serializers import CommandeSerializer
from .utils import TRANSITIONS

@api_view(['GET', 'POST'])
def commandes(request):

    if request.method == 'GET':

        commandes = Commande.objects.all()

        statut = request.GET.get(
            'statut'
        )

        fournisseur = request.GET.get(
            'fournisseur'
        )

        boutique_id = request.GET.get(
            'boutique_id'
        )

        if statut:

            commandes = commandes.filter(
                statut=statut
            )

        if fournisseur:

            commandes = commandes.filter(
                fournisseur_nom__icontains=fournisseur
            )

        if boutique_id:

            commandes = commandes.filter(
                boutique_id=boutique_id
            )

        serializer = CommandeSerializer(
            commandes,
            many=True
        )

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = CommandeSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=201
            )

        return Response(
            serializer.errors,
            status=400
        )
        

@api_view(['GET', 'DELETE'])
def commande_detail(request, id):

    try:

        commande = Commande.objects.get(
            id=id
        )

    except Commande.DoesNotExist:

        return Response(status=404)

    if request.method == 'GET':

        serializer = CommandeSerializer(
            commande
        )

        return Response(serializer.data)

    elif request.method == 'DELETE':

        if commande.statut != 'en_attente':

            return Response(
                {
                    "message":
                    "Suppression refusée"
                },
                status=409
            )

        commande.delete()

        return Response(status=200)
    
@api_view(['PATCH'])
def changer_statut(request, id):

    try:

        commande = Commande.objects.get(
            id=id
        )

    except Commande.DoesNotExist:

        return Response(status=404)

    nouveau_statut = request.data.get(
        'statut'
    )

    autorises = TRANSITIONS.get(
        commande.statut,
        []
    )

    if nouveau_statut not in autorises:

        return Response(
            {
                "message":
                "Transition interdite"
            },
            status=409
        )

    with transaction.atomic():

        commande.statut = nouveau_statut

        if nouveau_statut == 'livree':

            for ligne in commande.lignes.all():

                produit = ligne.produit

                produit.quantite_stock += (
                    ligne.quantite_commandee
                )

                produit.save()

            commande.date_livraison_reelle = (
                timezone.now()
            )

        commande.save()

    serializer = CommandeSerializer(
        commande
    )

    return Response(serializer.data)
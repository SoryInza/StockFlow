from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.conf import settings

from .models import Produit
from .serializers import ProduitSerializer


# GET ALL + POST
@api_view(['GET', 'POST'])
def produits(request):

    if request.method == 'GET':

        produits = Produit.objects.all()

        categorie = request.GET.get('categorie')
        statut = request.GET.get('statut')
        boutique_id = request.GET.get('boutique_id')

        if categorie:
            produits = produits.filter(categorie=categorie)

        if boutique_id:
            produits = produits.filter(boutique_id=boutique_id)

        if statut == 'alerte':
            produits = [
                p for p in produits if p.en_alerte
            ]

        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProduitSerializer(data=request.data)

        if request.data.get('sku')[:3] != settings.SKU:
            if serializer.is_valid():
                return Response(
                    serializer.data,
                    status=status.HTTP_400_BAD_REQUEST
                )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# GET ONE + PUT + DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def produit_detail(request, id):

    try:
        produit = Produit.objects.get(id=id)

    except Produit.DoesNotExist:
        return Response(
            {"message": "Produit introuvable"},
            status=404
        )

    if request.method == 'GET':

        serializer = ProduitSerializer(produit)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = ProduitSerializer(
            produit,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=400
        )

    elif request.method == 'DELETE':

        # Simulation commande active
        commande_active = False

        if commande_active:
            return Response(
                {"message": "Suppression refusée"},
                status=409
            )

        produit.delete()

        return Response(
            {"message": "Produit supprimé"}
        )


# PATCH STOCK
@api_view(['PATCH'])
def modifier_stock(request, id):

    try:
        produit = Produit.objects.get(id=id)

    except Produit.DoesNotExist:
        return Response(status=404)

    delta = request.data.get('delta')

    if delta is None:
        return Response(
            {"message": "delta requis"},
            status=400
        )

    nouveau_stock = produit.quantite_stock + int(delta)

    if nouveau_stock < 0:
        return Response(
            {"message": "Stock négatif interdit"},
            status=400
        )

    produit.quantite_stock = nouveau_stock
    produit.save()

    serializer = ProduitSerializer(produit)

    return Response(serializer.data)
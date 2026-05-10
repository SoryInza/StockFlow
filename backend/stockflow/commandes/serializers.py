from rest_framework import serializers
from django.utils import timezone

from .models import (
    Commande,
    LigneCommande
)

class LigneCommandeSerializer(
    serializers.ModelSerializer
):

    produit_nom = serializers.CharField(
        source='produit.nom',
        read_only=True
    )

    class Meta:

        model = LigneCommande

        fields = [
            'id',
            'produit',
            'produit_nom',
            'quantite_commandee',
            'prix_achat_unitaire'
        ]

    def validate_quantite_commandee(
        self,
        value
    ):

        if value <= 0:

            raise serializers.ValidationError(
                "Quantité invalide"
            )

        return value
    
    
class CommandeSerializer(
    serializers.ModelSerializer
):

    lignes = LigneCommandeSerializer(
        many=True
    )

    class Meta:

        model = Commande

        fields = '__all__'

    def validate_date_livraison_prevue(
        self,
        value
    ):

        if value <= timezone.now().date():

            raise serializers.ValidationError(
                "Date invalide"
            )

        return value

    def create(self, validated_data):

        lignes_data = validated_data.pop(
            'lignes'
        )

        commande = Commande.objects.create(
            **validated_data
        )

        for ligne in lignes_data:

            LigneCommande.objects.create(
                commande=commande,
                **ligne
            )

        return commande
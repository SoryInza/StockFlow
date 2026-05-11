from rest_framework import serializers
from .models import Produit
from django.conf import settings

class ProduitSerializer(serializers.ModelSerializer):

    en_alerte = serializers.ReadOnlyField()

    class Meta:
        model = Produit
        fields = '__all__'

    def validate_quantite_stock(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Le stock ne peut pas être négatif."
            )
        return value

    def validate_prix_unitaire(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Le prix doit être positif."
            )
        return value
    
    def validate_sku(
        self,
        value
    ):

        # LONGUEUR

        if len(value) != 8:

            raise serializers.ValidationError(

                "Format SKU invalide."
            )

        # FORMAT XXX-0000

        if value[3] != '-':

            raise serializers.ValidationError(

                "Le SKU doit respecter le format XXX-0000."
            )

        # PREFIXE

        prefix = value[:3]

        if prefix != settings.SKU:

            raise serializers.ValidationError(

                "Le SKU doit commencer par les trois premières lettres du prénom."
            )

        # PARTIE NUMERIQUE

        numbers = value[4:]

        if not numbers.isdigit():

            raise serializers.ValidationError(

                "Les 4 derniers caractères doivent être numériques."
            )
            
        if Produit.objects.filter(sku=value) != None:
            raise serializers.ValidationError(

                "Le produit existe deja."
            )
            
        return value
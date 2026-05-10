from rest_framework import serializers
from .models import Produit

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
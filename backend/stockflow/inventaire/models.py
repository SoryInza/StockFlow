from django.db import models

class Boutique(models.Model):
    nom = models.CharField(max_length=255)

class Produit(models.Model):

    sku = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=255)
    categorie = models.CharField(max_length=100)

    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    quantite_stock = models.IntegerField(default=0)
    seuil_alerte = models.IntegerField(default=0)

    boutique_id = models.ForeignKey(Boutique, models.CASCADE)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    @property
    def en_alerte(self):
        return (
            self.quantite_stock < self.seuil_alerte
            and self.seuil_alerte > 0
        )

    def __str__(self):
        return self.nom
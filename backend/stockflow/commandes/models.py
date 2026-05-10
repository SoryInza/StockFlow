from django.db import models
from django.utils import timezone

from inventaire.models import Boutique, Produit


class Commande(models.Model):

    STATUS_CHOICES = [

        ('en_attente', 'En attente'),

        ('confirmee', 'Confirmée'),

        ('livree', 'Livrée'),

        ('annulee', 'Annulée'),
    ]

    fournisseur_nom = models.CharField(
        max_length=255
    )

    fournisseur_contact = models.CharField(
        max_length=255
    )

    statut = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='en_attente'
    )

    date_livraison_prevue = models.DateField()

    date_livraison_reelle = models.DateTimeField(
        null=True,
        blank=True
    )

    boutique_id = models.ForeignKey(Boutique, models.CASCADE)

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"Commande {self.id}"


class LigneCommande(models.Model):

    commande = models.ForeignKey(
        Commande,
        related_name='lignes',
        on_delete=models.CASCADE
    )

    produit = models.ForeignKey(
        Produit,
        on_delete=models.CASCADE
    )

    quantite_commandee = models.IntegerField()

    prix_achat_unitaire = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):

        return f"Ligne {self.id}"
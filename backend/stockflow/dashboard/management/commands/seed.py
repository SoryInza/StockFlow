import random

from faker import Faker

from django.core.management.base import BaseCommand

from inventaire.models import Boutique, Produit
from commandes.models import (
    Commande,
    LigneCommande
)

fake = Faker('fr_FR')


class Command(BaseCommand):

    help = 'Peupler la base de données'

    def handle(self, *args, **kwargs):

        self.stdout.write(
            self.style.WARNING(
                'Suppression anciennes données...'
            )
        )

        LigneCommande.objects.all().delete()
        Commande.objects.all().delete()
        Produit.objects.all().delete()
        Boutique.objects.all().delete()
        
        # CREATION BOUTIQUES

        self.stdout.write(
            self.style.SUCCESS(
                'Création boutiques...'
            )
        )

        boutiques = []

        for i in range(3):

            boutique = Boutique.objects.create(

                nom=f'Boutique {i+1}',
            )

            boutiques.append(
                boutique
            )

        categories = [
            'Alimentaire',
            'Boissons',
            'Hygiène',
            'Électronique',
            'Maison'
        ]

        fournisseurs = [
            'Nestlé',
            'Orange',
            'Total',
            'Samsung',
            'Coca-Cola'
        ]

        produits = []

        self.stdout.write(
            self.style.SUCCESS(
                'Création produits...'
            )
        )
        
        boutiques = Boutique.objects.all()

        # PRODUITS

        for i in range(200):

            produit = Produit.objects.create(

                sku=f'INZ-{1000+i}',

                nom=fake.word().capitalize(),

                categorie=random.choice(categories),

                prix_unitaire=random.randint(
                    500,
                    50000
                ),

                quantite_stock=random.randint(
                    0,
                    100
                ),

                seuil_alerte=random.randint(
                    5,
                    20
                ),

                boutique_id=random.choice(boutiques)
            )

            produits.append(produit)

        self.stdout.write(
            self.style.SUCCESS(
                'Produits créés avec succès'
            )
        )

        # COMMANDES

        self.stdout.write(
            self.style.SUCCESS(
                'Création commandes...'
            )
        )

        statuts = [
            'en_attente',
            'confirmee',
            'livree',
            'annulee'
        ]

        for i in range(20):

            statut = random.choice(statuts)

            commande = Commande.objects.create(

                fournisseur_nom=random.choice(
                    fournisseurs
                ),

                fournisseur_contact=fake.email(),

                statut=statut,

                date_livraison_prevue=fake.date_between(
                    start_date='-10d',
                    end_date='+10d'
                ),

                boutique_id=random.choice(
        boutiques
    )
            )

            nb_lignes = random.randint(
                1,
                5
            )

            produits_selectionnes = random.sample(
                produits,
                nb_lignes
            )

            for produit in produits_selectionnes:

                quantite = random.randint(
                    1,
                    20
                )

                LigneCommande.objects.create(

                    commande=commande,

                    produit=produit,

                    quantite_commandee=quantite,

                    prix_achat_unitaire=random.randint(
                        300,
                        40000
                    )
                )

                # Mise à jour stock si livrée

                if statut == 'livree':

                    produit.quantite_stock += quantite

                    produit.save()

        self.stdout.write(
            self.style.SUCCESS(
                'Commandes créées avec succès'
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                'Base de données peuplée avec succès !'
            )
        )
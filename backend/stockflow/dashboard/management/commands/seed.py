import random

from faker import Faker

from django.core.management.base import BaseCommand

from inventaire.models import (
    Boutique,
    Produit
)

from commandes.models import (
    Commande,
    LigneCommande
)

fake = Faker('fr_FR')


class Command(BaseCommand):

    help = 'Peupler la base de données'

    def handle(self, *args, **kwargs):

        # SUPPRESSION DONNEES

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

                nom=f'Boutique {i+1}'
            )

            boutiques.append(
                boutique
            )

        # DONNEES

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

        produits_to_fetch = [

            "Riz",
            "Sucre",
            "Huile",
            "Savon",
            "Dentifrice",
            "Shampoing",
            "Lait",
            "Yaourt",
            "Farine",
            "Beurre",
            "Fromage",
            "Chocolat",
            "Biscuit",
            "Café",
            "Thé",
            "Jus",
            "Eau minérale",
            "Soda",
            "Spaghetti",
            "Tomate",
            "Oignon",
            "Pomme de terre",
            "Poisson",
            "Poulet",
            "Viande",
            "Sel",
            "Poivre",
            "Mayonnaise",
            "Ketchup",
            "Moutarde",
            "Gel douche",
            "Déodorant",
            "Parfum",
            "Crème hydratante",
            "Lessive",
            "Éponge",
            "Balai",
            "Seau",
            "Ampoule",
            "Chargeur",
            "Écouteurs",
            "Clavier",
            "Souris",
            "Téléphone",
            "Tablette",
            "Ordinateur",
            "Ventilateur",
            "Mixeur",
            "Micro-ondes",
            "Réfrigérateur",

            "Caméra",
            "Casque audio",
            "Montre",
            "Batterie",
            "Routeur",
            "Câble USB",
            "Imprimante",
            "Scanner",
            "Projecteur",
            "Smart TV",
            "Congélateur",
            "Plaque chauffante",
            "Four",
            "Machine à laver",
            "Fer à repasser",
            "Bouilloire",
            "Tasse",
            "Assiette",
            "Cuillère",
            "Fourchette",
            "Couteau",
            "Plateau",
            "Bouteille",
            "Gobelet",
            "Papier toilette",
            "Serviette",
            "Mouchoir",
            "Gel antiseptique",
            "Brosse à dents",
            "Coton",
            "Bandage",
            "Aspirine",
            "Vitamine C",
            "Savon liquide",
            "Lotion",
            "Huile de coco",
            "Huile d’olive",
            "Miel",
            "Confiture",
            "Céréales",
            "Pain",
            "Croissant",
            "Pizza",
            "Hamburger",
            "Sandwich",
            "Hot dog",
            "Frites",
            "Poulet rôti",
            "Steak",
            "Saucisse",

            "Chaise",
            "Table",
            "Canapé",
            "Lit",
            "Oreiller",
            "Matelas",
            "Rideau",
            "Lampe",
            "Tapis",
            "Armoire",
            "Bureau",
            "Bibliothèque",
            "Stylo",
            "Crayon",
            "Gomme",
            "Cahier",
            "Livre",
            "Sac à dos",
            "Calculatrice",
            "Agrafeuse",
            "Marqueur",
            "Feuille A4",
            "Enveloppe",
            "Cartable",
            "Dictionnaire",
            "Chargeur solaire",
            "Power bank",
            "Drone",
            "Webcam",
            "Microphone",
            "Clé USB",
            "Disque dur",
            "SSD",
            "Carte mémoire",
            "Manette",
            "Console",
            "Jeu vidéo",
            "Lunettes",
            "Chaussures",
            "Sandales",
            "T-shirt",
            "Chemise",
            "Jean",
            "Pantalon",
            "Veste",
            "Pull",
            "Casquette",
            "Ceinture",
            "Sac à main",

            "Bracelet",
            "Collier",
            "Bague",
            "Boucles d’oreilles",
            "Montre connectée",
            "Parapluie",
            "Valise",
            "Bouteille thermique",
            "Glacière",
            "Ventouse",
            "Marteau",
            "Tournevis",
            "Perceuse",
            "Scie",
            "Pince",
            "Clou",
            "Vis",
            "Peinture",
            "Pelle",
            "Arrosoir",
            "Engrais",
            "Graine",
            "Tondeuse",
            "Brouette",
            "Corde",
            "Filet",
            "Extincteur",
            "Détecteur fumée",
            "Caméra sécurité",
            "Alarme",
            "Serrure",
            "Cadenas",
            "Batterie externe",
            "Ventilateur USB",
            "Mini frigo",
            "Radio",
            "Télécommande",
            "Adaptateur",
            "Multiprise",
            "Coffre-fort",
            "Calculatrice scientifique",
            "Scanner portable",
            "Toner",
            "Cartouche encre",
            "Papier photo",
            "Trépied",
            "Objectif photo",
            "Sac photo",
            "Éclairage LED",
            "Projecteur LED",

            "Chaîne Hi-Fi",
            "Écran PC",
            "Support écran",
            "Climatiseur",
            "Purificateur air",
            "Diffuseur parfum",
            "Horloge",
            "Calendrier",
            "Agenda",
            "Carnet",
            "Puzzle",
            "Jeu éducatif",
            "Ballon",
            "Raquette",
            "Chaussures sport",
            "Tapis yoga",
            "Haltère",
            "Vélo",
            "Trottinette",
            "Casque vélo",
            "Gourde",
            "Boussole",
            "GPS",
            "Carte routière",
            "Chargeur voiture",
            "Aspirateur",
            "Robot cuisine",
            "Machine café",
            "Cafetière",
            "Grille-pain",
            "Mixeur plongeant",
            "Cocotte",
            "Poêle",
            "Marmite",
            "Boîte conservation",
            "Film alimentaire",
            "Papier aluminium",
            "Sac congélation",
            "Détergent",
            "Nettoyant vitres",
            "Désodorisant",
            "Lingette",
            "Écharpe",
            "Gants",
            "Bonnet",
            "Pyjama",
            "Chaussette",
            "Sous-vêtement",
            "Costume",
            "Cravate",

            "Robe",
            "Jupe",
            "Short",
            "Maillot",
            "Bikini",
            "Serviette plage",
            "Chaise pliante",
            "Table pliante",
            "Tente",
            "Sac couchage",
            "Lampe torche",
            "Pile",
            "Briquet",
            "Allumettes",
            "Thermos",
            "Machine soda",
            "Extracteur jus",
            "Mini enceinte",
            "Écouteurs Bluetooth",
            "Smartphone",
            "PC Gamer",
            "Routeur WiFi",
            "Hub USB",
            "Switch réseau",
            "Câble HDMI",
            "Moniteur",
            "Clavier gamer",
            "Souris gamer",
            "Tapis souris",
            "Fauteuil bureau",
            "Support téléphone",
            "Anneau lumière",
            "Stabilisateur",
            "Caméscope",
            "Lecteur DVD",
            "Disque Blu-ray",
            "Radio réveil",
            "Mini ventilateur",
            "Machine glace",
            "Cuiseur riz",
            "Balance cuisine",
            "Balance électronique",
            "Thermomètre",
            "Tensiomètre",
            "Oxymètre",
            "Pèse personne",
            "Ciseaux",
            "Colle",
            "Ruban adhésif",
            "Perforatrice"
        ]

        produits = []

        # CREATION PRODUITS

        self.stdout.write(

            self.style.SUCCESS(

                'Création produits...'
            )
        )

        for index in range(200):

            random_index = random.randint(

                0,
                len(produits_to_fetch) - 1
            )

            produit = Produit.objects.create(

                    sku=f'INZ-{1000+index}',

                    nom=produits_to_fetch[
                        random_index
                    ],

                    categorie=random.choice(
                        categories
                    ),

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

                    boutique_id=random.choice(
                        boutiques
                    )
                )

            produits.append(
                    produit
                )

        self.stdout.write(

            self.style.SUCCESS(

                f'{len(produits)} produits créés'
            )
        )

        # SECURITE

        if len(produits) < 5:

            raise Exception(

                "Pas assez de produits créés."
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

            statut = random.choice(
                statuts
            )

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

                # MAJ STOCK SI LIVREE

                if statut == 'livree':

                    produit.quantite_stock += (
                        quantite
                    )

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
Gestion de Stock API

1. Présentation du projet

Cette application permet de gérer le stock de produits d’un magasin.
Elle offre la possibilité de :

ajouter des produits ;
modifier le stock ;
suivre les commandes ;
détecter les produits en rupture ;
gérer le statut des commandes.
Le projet a été développé avec :

Python
SQLite
Django
HTML/CSS
JavaScript

Raison ces choix ?
Django : framework léger et simple pour créer rapidement une API REST ;
SQLite : base de données facile à utiliser pour un projet de petite taille ;
Python : langage rapide à développer et très utilisé pour le back-end.
HTML/CSS/JS: permettent de créer une interface légère et responsive.
Aussi se sont les consigne de l'exercice

2. Prérequis

Avant de lancer le projet, il faut installer :

Python 3.10+
pip
SQLite

3. Installation et lancement

- Cloner le projet

        bash
        Copier le code
        git clone https://github.com/user/stock-api.git

- Entrer dans le dossier

        bash
        Copier le code
        cd stockflow

- Installer les dépendances

        bash
        Copier le code
        pip install -r requirements.txt

- Lancer le serveur

        bash
        Copier le code
        python manage.py runserver
        Le serveur démarre sur :

        Copier le code
        http://127.0.0.1:8000

4. Documentation des endpoints

Ajouter un produit

        Méthode : POST
        Route :

    Copier le code

        /api/products
        Exemple de body
        json

    Copier le code
        {
        "sku": "P001",
        "name": "Clavier",
        "stock": 10
        }
    Exemple de réponse
        json
        Copier le code
        {
        "message": "Produit ajouté avec succès"
        }

Mettre à jour le stock

        Méthode : PUT
        Route :
        txt
    Copier le code
        /api/products/update-stock
        Exemple de body
        json
    Copier le code
        {
        "sku": "P001",
        "quantity": 5
        }
        Exemple de réponse
        json
    Copier le code
        {
        "message": "Stock mis à jour"
        }

5. Ce qui est fait / ce qui ne l’est pas

- Ce qui est fait

        gestion des produits ;
        mise à jour du stock ;
        gestion des commandes ;
        alertes de rupture.

- Ce qui ne l'est pas

        authentification utilisateur ;
        interface graphique ;
        notifications automatiques.

6. Difficultés rencontrées

Gestion des transactions SQL
Au début, certaines modifications n’étaient pas sauvegardées correctement.
Le problème a été résolu avec conn.commit() et les transactions.

Gestion des erreurs
Certaines erreurs faisaient arrêter le programme brutalement.
Des blocs try/except ont été ajoutés pour améliorer la stabilité.

Organisation du code
Le projet devenait difficile à maintenir.
Le code a été séparé en plusieurs fonctions pour le rendre plus lisible.

7. Ce que je ferais différemment

Avec plus de temps, j’aimerais :

- ajouter une authentification JWT ;
- créer une interface web ;
- améliorer la sécurité ;
- écrire des tests automatiques ;
- utiliser PostgreSQL à la place de SQLite.

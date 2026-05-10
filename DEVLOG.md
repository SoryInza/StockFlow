# DEVLOG — STOCKFLOW

---

# Samedi — Matin

Heure :
09h00 → 12h30

## Accompli

- Lecture complète du sujet technique
- Analyse des besoins fonctionnels
- Étude des modules :
  - inventaire
  - commandes fournisseurs
  - dashboard
  - statistiques
- Initialisation du projet Django
- Installation des dépendances :
  - Django REST Framework
  - django-cors-headers
  - Faker
- Création des applications :
  - inventaire
  - dashboard
  - statistiques
- Création des premiers modèles :
  - Boutique
  - Produit

## Problème rencontré

Erreur lors des migrations :

```txt
No module named rest_framework
```

## Solution

Installation du package manquant :

```bash
pip install djangorestframework
```

## Choix technique

Choix de Django REST Framework pour accélérer la création des APIs REST et structurer proprement le backend.

---

# Samedi — Après-midi

Heure :
14h00 → 18h30

## Accompli

- Création des modèles :
  - Commande
  - LigneCommande
- Mise en place des relations :
  - Produit ↔ LigneCommande
  - Boutique ↔ Produit
  - Boutique ↔ Commande
- Création des serializers DRF
- Développement des endpoints produits :
  - GET /api/produits
  - GET /api/produits/:id
  - POST /api/produits
  - PUT /api/produits/:id
  - PATCH /api/produits/:id/stock
  - DELETE /api/produits/:id

## Problème rencontré

Le champ :

```python
en_alerte
```

retournait toujours False même avec un stock faible.

## Solution

Ajout de la logique :

```python
quantite_stock < seuil_alerte
```

dans le serializer.

## Choix technique

Calcul dynamique de `en_alerte` afin d’éviter un stockage inutile dans la base de données.

---

# Samedi — Soir

Heure :
20h00 → 00h30

## Accompli

- Développement des endpoints commandes :
  - GET /api/commandes
  - POST /api/commandes
  - PATCH /api/commandes/:id/statut
  - DELETE /api/commandes/:id
- Mise en place des règles de transition :
  - en_attente → confirmee
  - en_attente → annulee
  - confirmee → livree
- Tests Postman des endpoints

## Problème rencontré

Les commandes livrées pouvaient encore changer de statut.

## Solution

Ajout d’une validation des transitions autorisées.

## Choix technique

Utilisation de PATCH pour les changements partiels conformément aux standards REST.

---

# Dimanche — Matin

Heure :
08h30 → 12h00

## Accompli

- Développement du dashboard backend
- Création endpoint :
  - GET /api/dashboard
- Calcul :
  - total produits
  - produits en alerte
  - ruptures
  - valeur stock
  - commandes en retard
- Tri des alertes critiques

## Problème rencontré

Les alertes critiques n’étaient pas triées correctement.

## Solution

Utilisation de :

```python
sorted(alertes, key=lambda x: x['deficit'])
```

## Choix technique

Retour d’un JSON unique regroupant toutes les statistiques pour limiter les appels frontend.

---

# Dimanche — Après-midi

Heure :
14h00 → 18h00

## Accompli

- Création du frontend Dashboard
- Création du frontend Inventaire
- Connexion API ↔ frontend avec Fetch API
- Ajout :
  - tableau produits
  - filtres
  - ajout produit
  - ajustement stock
  - suppression produit
- Création des badges de statut

## Problème rencontré

Erreur navigateur :

```txt
ERR_CONNECTION_REFUSED
```

## Solution

Le serveur Django n’était pas démarré.

Commande utilisée :

```bash
python manage.py runserver
```

## Choix technique

Frontend en HTML/CSS/JS pur pour respecter les contraintes du sujet et garder un projet léger.

---

# Dimanche — Soir

Heure :
20h00 → 01h00

## Accompli

- Création du frontend Commandes
- Ajout des formulaires dynamiques
- Création du système :
  - ajout ligne commande
  - changement statut
  - commandes en retard
- Création navbar responsive
- Navigation entre :
  - dashboard
  - inventaire
  - commandes

## Problème rencontré

La navbar fixed cachait le contenu des pages.

## Solution

Ajout de :

```css
body {
  padding-top: 110px;
}
```

## Choix technique

Navbar JavaScript réutilisable afin d’éviter la duplication du code HTML.

---

# Lundi — Nuit / Très tôt matin

Heure :
01h30 → 05h30

## Accompli

- Développement module statistiques
- Intégration Chart.js
- Graphiques :
  - produits par catégorie
  - commandes livrées
  - commandes en attente
- Création du script seed
- Génération automatique :
  - produits
  - commandes
  - stocks
  - fournisseurs
- Tests complets de l’application
- Vérification responsive mobile
- Nettoyage du code
- Vérification des endpoints
- Rédaction du DEVLOG

## Problème rencontré

Erreur :

```txt
Cannot assign "1": "Produit.boutique" must be a "Boutique" instance
```

## Solution

Utilisation de :

```python
random.choice(boutiques)
```

au lieu de :

```python
boutique_id=random.randint(1,2)
```

## Choix technique

Utilisation de Faker pour créer rapidement des données réalistes et tester les dashboards ainsi que les statistiques.

---

# Lundi — Finalisation

Heure :
05h30 → 06h45

## Accompli

- Derniers tests manuels
- Vérification des routes API
- Vérification des transitions commandes
- Vérification dashboard
- Vérification statistiques
- Organisation des dossiers
- Préparation du rendu final

## Problème rencontré

Certaines suppressions de produits étaient autorisées malgré des commandes actives.

## Solution

Ajout d’une vérification avant suppression avec retour HTTP 409.

## Choix technique

Protection des données métier afin de conserver l’intégrité des commandes fournisseurs.

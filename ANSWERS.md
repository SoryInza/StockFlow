1 — Injection SQL (ligne 7)

La requête SQL est construite avec de la concaténation de chaînes.  
Cela peut permettre une injection SQL via `sku` ou `quantity`.

Pour éviter ce problème, il vaut mieux utiliser des requêtes paramétrées.

Correction

python
query = "UPDATE products SET stock=? WHERE sku=?"
conn.execute(query, (quantity, sku))

2 — Mauvaise gestion de la connexion (lignes 5 à 10)

Si une erreur survient avant `conn.close()`, la connexion peut rester ouverte.  
Il serait plus propre d’utiliser un context manager avec `with`.

Correction

```python
with sqlite3.connect(db_path) as conn:
    conn.execute(query, (quantity, sku))
    conn.commit()
```

3— Duplication des alertes (ligne 18)

Le même produit est ajouté plusieurs fois dans la liste `alerts`.  
Cela peut créer des doublons et fausser les résultats.

Correction

```python
alerts.append(products[i])
```

4— Boucle peu lisible (ligne 15)

L’utilisation de `range(len(products))` n’est pas vraiment nécessaire ici.  
Une boucle directe est plus simple à lire et plus propre.

Correction proposée

```python
for product in products:
```

5 — Risque de KeyError (lignes 16 et 24)

Le code suppose que certaines clés existent toujours dans les dictionnaires (`stock`, `threshold`, `priority`, etc.).  
Si une clé manque, le programme peut planter.

Correction proposée

```python
product.get('stock', 0)
```

6— Absence de validation métier (ligne 24)

Le stock peut devenir négatif ou incohérent si `ordered_qty` contient une mauvaise valeur.

Il faut vérifier les quantités avant la mise à jour.

Correction

```python
if item['ordered_qty'] <= 0:
    raise ValueError("Quantité invalide")
```

7 — Modification non sauvegardée (ligne 27)

La ligne :

```python
order['status'] = 'livree'
```

modifie uniquement l’objet Python en mémoire.  
Le changement n’est pas enregistré dans la base de données.

Correction

```python
UPDATE orders SET status='livree' WHERE id=?
```

8 — Absence de gestion d’erreurs

Aucune exception n’est gérée dans le fichier.  
En cas de problème, le programme peut s’arrêter brutalement sans afficher d’erreur claire.

Correction proposée

```python
try:
    ...
except Exception as e:
    print(e)
```

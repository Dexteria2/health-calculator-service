# Nicolas GUERIN
# Health Calculator Microservice

## Description du projet
Le **Health Calculator Microservice** est une application Python qui fournit des calculs de santé tels que l'indice de masse corporelle (BMI) et le taux métabolique basal (BMR) via une API REST. Cette application est conteneurisée avec Docker et est déployée sur Azure App Service à l'aide de workflows CI/CD GitHub Actions.

---

## Fonctionnalités principales

### Endpoints

1. **`/bmi`** :
   - Méthode : `POST`
   - Entrée : JSON contenant `height` (en mètres) et `weight` (en kilogrammes).
   - Sortie : BMI calculé arrondi à 2 décimales.

   Exemple de requête :
   ```bash
   curl -X POST https://health-calculator-app-nico-euephjaagvd4aset.francecentral-01.azurewebsites.net/bmi \
   -H "Content-Type: application/json" \
   -d '{"weight": 70, "height": 1.75}'
   ```
   Réponse attendue :
   ```json
   {
       "BMI": 22.86
   }
   ```

2. **`/bmr`** :
   - Méthode : `POST`
   - Entrée : JSON contenant `height` (en cm), `weight` (en kg), `age` (en années), et `gender` ("male" ou "female").
   - Sortie : BMR calculé arrondi à 2 décimales.

   Exemple de requête :
   ```bash
   curl -X POST https://health-calculator-app-nico-euephjaagvd4aset.francecentral-01.azurewebsites.net/bmr \
   -H "Content-Type: application/json" \
   -d '{"weight": 70, "height": 175, "age": 25, "gender": "male"}'
   ```
   Réponse attendue :
   ```json
   {
       "BMR": 1724.05
   }
   ```

---

## Structure des fichiers

1. **`app.py`**
   - Fournit les endpoints `/bmi` et `/bmr`.
   - Valide les entrées JSON et gère les erreurs si les données sont manquantes ou invalides.
   - Appelle les fonctions utilitaires de `health_utils.py` pour effectuer les calculs.

2. **`health_utils.py`**
   - Contient les fonctions de calcul :
     - `calculate_bmi(height, weight)` : Calcule le BMI en utilisant la formule `weight / (height^2)`.
     - `calculate_bmr(height, weight, age, gender)` : Calcule le BMR en utilisant l'équation de Harris-Benedict.
   - Gère les cas d'erreurs comme les entrées négatives ou un sexe invalide.

3. **`test.py`**
   - Implémente des tests unitaires pour valider la logique de calcul du BMI et du BMR.
   - Utilise le framework `unittest`.

4. **`requirements.txt`**
   - Spécifie les dépendances nécessaires, notamment Flask et Gunicorn.
   - Commande d'installation : `pip install -r requirements.txt`.

5. **`Dockerfile`**
   - Définit l'image Docker pour l'application.
   - Étapes principales :
     - Copie les fichiers de l'application.
     - Installe les dépendances à partir de `requirements.txt`.
     - Définit Gunicorn comme serveur d'application.
   - Permet de déployer l'application de manière portable.

6. **`Makefile`**
   - Automatisation des tâches courantes :
     - `make init` : Initialise l'environnement virtuel et installe les dépendances.
     - `make run` : Lance l'application Flask en local.
     - `make build` : Construit l'image Docker.
     - `make run-container` : Exécute l'application dans un conteneur Docker.
     - `make test` : Exécute les tests unitaires.
     - `make test-api` : Effectue un test rapide des endpoints API.

7. **`ci.yml`** (Pipeline CI)
   - Exécute automatiquement les tests à chaque push sur la branche principale.
   - Étapes principales :
     - Installe les dépendances.
     - Exécute les tests définis dans `test.py`.

8. **`cd.yml`** (Pipeline CD)
   - Déploie automatiquement l'application sur Azure App Service après un push sur `main`.
   - Étapes principales :
     - Archive les fichiers de l'application dans un fichier zip.
     - Déploie l'application en utilisant `az webapp deployment`.

---

## Tests à effectuer pour démontrer le bon fonctionnement

1. **Test de l'API `/bmi`**
   - Commande :
     ```bash
     curl -X POST https://health-calculator-app-nico-euephjaagvd4aset.francecentral-01.azurewebsites.net/bmi \
     -H "Content-Type: application/json" \
     -d '{"weight": 70, "height": 1.75}'
     ```
   - Résultat attendu :
     ```json
     {
         "BMI": 22.86
     }
     ```

2. **Test de l'API `/bmr`**
   - Commande :
     ```bash
     curl -X POST https://health-calculator-app-nico-euephjaagvd4aset.francecentral-01.azurewebsites.net/bmr \
     -H "Content-Type: application/json" \
     -d '{"weight": 70, "height": 175, "age": 25, "gender": "male"}'
     ```
   - Résultat attendu :
     ```json
     {
         "BMR": 1724.05
     }
     ```

---

## Fonctionnement des workflows CI/CD

1. **CI Pipeline**
   - Exécute les tests unitaires pour valider la logique métier à chaque push sur `main`.
   - Garantit que l'application est stable avant déploiement.

2. **CD Pipeline**
   - Déploie automatiquement l'application sur Azure App Service après validation des tests CI.
   - Permet une livraison continue sans intervention manuelle.

---

## Commandes Makefile utiles

- **Initialisation** :
  ```bash
  make init
  ```
- **Lancer en local** :
  ```bash
  make run
  ```
- **Construire l'image Docker** :
  ```bash
  make build
  ```
- **Exécuter dans un conteneur Docker** :
  ```bash
  make run-container
  ```
- **Exécuter les tests** :
  ```bash
  make test
  ```


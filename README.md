## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

#### Déploiement
Le déploiement est automatiquement déclenché par la pipeline CircleCI lors d'un *push* sur la branche 'master' du dépôt GitHub.
Il est nécessaire de lier le dépôt utilisé à un compte CircleCI. La pipeline est gouvernée par le fichier `config.yml` dans le dossier `.circleci`

Le déploiement utilise l'orbe CircleCI adaptée pour un déploiement sur Heroku, et une fois déployé, applique les migrations sur la base de données du site sur Heroku.

##### Configuration requise
Pour que le déploiement se passe correctement, il est nécessaire que l'application Heroku dispose de 4 variables d'environnement:
- DATABASE_URL, qui est automatiquement générée par l'application heroku lors de la création de la base de données avec la commande `heroku addons:create heroku-postgresql:hobby-dev` (N.B: hobby-dev peut être remplacé par un des autres plans de Heroku).
- DJANGO_KEY, qui correspond à la clé secrète du projet Django et qui doit être initialisée manuellement avec la commande `heroku config:set DJANGO_KEY=<clé>`
- ENV, qui doit être la chaîne de caractère `production` (N.B : La chaîne est sensible à la casse!), et qui doit être initialisée comme au-dessus.
- SENTRY_ID, qui doit être la clé du compte Sentry qui recevra les logs d'erreurs. Elle doit elle aussi être initialisée comme les deux variables précédentes.

N.B : Ces variables ne doivent être initialisées qu'une fois, à la création de l'application Heroku.

#### Déployer
- Si l'application existe déjà:
Il suffit de lancer la pipeline CircleCI. Celle-ci peut être lancée manuellement sur l'application CircleCI, ou être automatiquement lancée par un *push* sur la branche 'master' du dépôt GitHub.

- Si l'application n'existe pas ou plus:
Après avoir lancé la pipeline CircleCI comme au-dessus, il faut initialiser le contenu de la base de données (sauf bien entendu si vous voulez remettre à zéro la base de données).
Pour cela, il vous faut ajouter un fichier JSON (e.g : `data.json`) qui contient les données dans le dépôt. Un moyen d'en obtenir un est d'utiliser la commande *dumpdata* sur la base de données.
Une fois la pipeline exécutée et l'application en ligne, utilisez la commande `heroku run -a <nom_de_l_application> python manage.py loaddata <nom_du_fichier_JSON>`, par exemple `heroku run -a oc-lettings-cbravo python manage.py loaddata data.json`


### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

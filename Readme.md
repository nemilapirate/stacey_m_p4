# Projet 4 : Création d'un tournoi d'échec avec Python

## Installation

Pré-requis : Python3

Dossier Git à cloner pour lancer le programme :
    https://github.com/nemilapirate/stacey_m_p4.git

A partir du répertoire stacey_m_p4 :
1) Créer un environnement virtuel avec la commande : python -m venv env

2) Activer l'environnement virtuel.
    Sous windows :
        env/Scripts/activate.bat
    sous linux et mac OS:
        source env/bin/activate

3) Installer les packages requis pour l'application avec la commande :
    pip install -r requirements.txt

4) Lancer le script avec la commande :
    python main.py

### Présentation de l'application

Le menu principal donne accès à plusieurs options.

#### 1. Créer un tournoi.
L'option 1 permet de créer un tournoi puis de créer des joueurs
et enfin lancer le tournois avec les joueurs précedement créer.

    * Lors de la création du tournoi, il faudra saisir les informations 
      comme le nom du tournoi, le nombre de joueurs etc...
    * Ensuite créer les joueurs avec leurs informations 
      et enfin lancer le match.
    * Le tournoi et les joueurs seront automatiquement sauvegarder 
      dans la base de données, ce qui permet de reprendre un tournoi.

##### 2. Charger un tournoi.
Cette option permet de charger un tournoi qui est sauvegarder
dans la base de données.
Une fois séléctionner, vous pourrez commencer le tournoi.

##### 3. Voir les rapports.
Cette option permet de générer différents rapports:
    * Consulter le classement global des joueurs,
      par rang ou bien par ordre alphabétique.
    * Voir les détails des tournois précedement jouer,
      le classement des joueurs, les tours et matchs pour chaque tournois.

###### 4. Générer un rapport flake8
Flake8 est un outil pour aider à valider un code python au regarde de la PEP 8.
C'est à dire un ensemble de regles qui permet d'homogéniser son code et d'appliquer les bonnes pratiques.

    * Pour installer flake8-HTML
        Dans le terminal faite la commande :
            pip install flake8-html

    * Pour avoir un rapport index HTML
        Dans le terminal faite la commande :
            flake8 --format=html --htmldir=flake-report

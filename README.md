# Projet4 : Développez un programme logiciel en Python

## Présentation

Le logiciel permet le suivi de tournois d'échec et des joueurs qui y participent. 
La base de données est alimentée par l'utilisateur qui peut retrouver les informations saisies en ouvrant les fichiers de données ou en ouvrant les rapports qu'il a édité.

## Prérequis à l'utilisation

- Le logiciel est utilisable hors-ligne

- Python3 doit être installé sur votre ordinateur (v3.12.3). Vous pouvez vérifier votre version en tapant la commande python3 -v Pour installer Python sous Windows, téléchargez l'installateur correspndant à votre systeme via le lien suivant : https://www.python.org/downloads/windows/ Sous linux, exécutez la fonction apt install python3

- Pour l'installation des dépendances vous devez disposer de l'installateur pip si vous utilisez un environnement virtuel ou utilisez la commande apt install python3-xyz en remplaçant xyz par le nom de la dépendance souhaitée. La liste des dépendances nécessaires est disponible dans le fichier requierements.txt

- Git est également nécessaire pour cloner le projet sur votre machine. Pour installer la version de Git adaptée à votre configuration suivez le lien suivant et lancer l'installateur: https://git-scm.com/downloads

## Installer le programme

- Utilisez la commande suivante pour télécharger le programme. ''git clone https://github.com/SylvainNogrette/Projet2.git](https://github.com/SylvainNogrette/OC-Projet4.git''
- Installer les dépendances TinyDB et questionary. Vous pouvez retrouver la liste des dépendances dans le fichier requierement.text Vous pouvez installer ces dépendances manuellement ou utiliser la commande pip install -r requierements.txt depuis le dossier de travail.

## Utiliser le programme

Dans le dossier de travail, taper la commande : " python3 main.py " pour exécuter le logiciel.

- Commencez par Ajouter des joueurs à la base de données.
- Vous pouvez ensuite créer un tournoi
- Inscrivez les joueurs au tournoi
- Au fur et à mesure du tournoi, démarrez un round et renseignez les scores à la fin du round.
- Vous avez la possibilité de créer des rapports en format .txt
- Lorsque vous quittez l'application, les données sont persistent dans les fichiers .json dans le dossier Base de Données.

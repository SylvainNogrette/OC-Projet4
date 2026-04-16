import questionary

import Constants


def display_main_menu():

    questionary.text("Bienvenu dans le Gestionnaire de Club d'échec.")
    return questionary.select(
        "Sélectionnez le menu auquel vous souhaitez accéder",
        choices=[
                Constants.PLAYER_MENU,
                Constants.TOURNAMENT_MENU,
                Constants.REPORT_MENU,
                Constants.EXIT
                ]).ask()


def display_player_menu():
    return questionary.select(Constants.ASK_CHOICE,
                              choices=[
                                    "Ajouter un utilisateur",
                                    "Supprimer un ou des joueurs",
                                    Constants.RETURN_TO_MAIN
                                    ]).ask()


def display_tournament_menu():
    print(Constants.TOURNAMENT_MENU)
    return questionary.select(Constants.ASK_CHOICE,
                              choices=[
                                  "Ajouter un tournoi",
                                  "Ajouter des joueurs au tournoi",
                                  "Démarrer un Round",
                                  Constants.RETURN_TO_MAIN
                              ]).ask()


def display_report_menu():
    print(Constants.REPORT_MENU)
    return questionary.select(Constants.ASK_CHOICE,
                              choices=[
                                  "Joueurs par ordre alphabétique",
                                  "Tous les tournois",
                                  "Nom et date du tournoi",
                                  "Joueurs dans le tournoi",
                                  "Historique des matchs du tournoi",
                                  Constants.RETURN_TO_MAIN
                                  ]).ask()

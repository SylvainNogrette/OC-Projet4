import questionary

import constants


def display_main_menu():

    questionary.text("Bienvenu dans le Gestionnaire de Club d'échec.")
    return questionary.select(
        "Sélectionnez le menu auquel vous souhaitez accéder",
        choices=[
                constants.PLAYER_MENU,
                constants.TOURNAMENT_MENU,
                constants.REPORT_MENU,
                constants.EXIT
                ]).ask()


def display_player_menu():
    return questionary.select(constants.ASK_CHOICE,
                              choices=[
                                    "Ajouter un utilisateur",
                                    "Supprimer un ou des joueurs",
                                    constants.RETURN_TO_MAIN
                                    ]).ask()


def display_tournament_menu():
    print(constants.TOURNAMENT_MENU)
    return questionary.select(constants.ASK_CHOICE,
                              choices=[
                                  "Ajouter un tournoi",
                                  "Ajouter des joueurs au tournoi",
                                  "Démarrer un Round",
                                  constants.RETURN_TO_MAIN
                              ]).ask()


def display_report_menu():
    print(constants.REPORT_MENU)
    return questionary.select(constants.ASK_CHOICE,
                              choices=[
                                  "Joueurs par ordre alphabétique",
                                  "Tous les tournois",
                                  "Nom et date du tournoi",
                                  "Joueurs dans le tournoi",
                                  "Historique des matchs du tournoi",
                                  constants.RETURN_TO_MAIN
                                  ]).ask()

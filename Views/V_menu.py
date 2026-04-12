import questionary

import Constants


Constants.RETURN_TO_MAIN = "Revenir au menu principal"


def display_main_menu():

    questionary.text("Bienvenu dans le Gestionnaire de Club d'échec.")
    return questionary.select(
        "Sélectionnez le menu auquel vous souhaitez accéder",
        choices=[
                Constants.PLAYER_MENU,
                Constants.TOURNAMENT_MENU,
                Constants.REPORT_MENU,
                Constants.SAVE_MENU,
                Constants.EXIT
                ]).ask()


def display_player_menu():
    return questionary.select(Constants.ASK_CHOICE,
                              choices=[
                                    "Ajouter un utilisateur",
                                    "Modifier un joueur existant",
                                    "Supprimer un ou des joueurs",
                                    Constants.RETURN_TO_MAIN
                                    ]).ask()


def display_tournament_menu():
    print(Constants.TOURNAMENT_MENU)
    return questionary.select(Constants.ASK_CHOICE,
                              choices=[
                                  "Ajouter un tournoi",
                                  "Ajouter des joueurs au tournoi",
                                  "Fin d'un tournoi",
                                  "Gestion des matches",
                                  Constants.RETURN_TO_MAIN
                              ]).ask()


def display_match_menu():
    print(Constants.MATCH_MENU)
    return questionary.select(Constants.ASK_CHOICE,
                              choices=[
                                        "Démarrer un Round",
                                        Constants.RETURN_TO_MAIN
                                ]).ask()


def display_save_menu():
    print(Constants.SAVE_MENU)
    return questionary(Constants.ASK_CHOICE,
                       choices=[
                           "Creer une sauvegarde",
                           "Restaurer une sauvegarde",
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


def ask_which_attr_to_modify(dict):
    return questionary.select("Quel paramètre voulez vous modifier?",
                              choices=dict).ask()


def ask_modification_value(quoiModifier, quiModifier):
    return questionary.text("Saisissez la modification à\
                                     apporter à {} du joueur {}".format(
                                           quoiModifier, quiModifier)).ask()


def ask_save_to_restore(list_of_saves: list[str]):
    return questionary.select("Quelle sauvegarde souhaitez-vous restaurer?",
                              choices=list_of_saves).ask()


def ask_name_for_save():
    return questionary.text(
        "Quel nom souhaitez-vous donner à votre sauvegarde?"
        )

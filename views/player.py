import questionary


from controls.player import remove_players
from controls.player import get_every_players_in_db


def select_players_in_DB():
    list_registered_player = []
    print("Assurez-vous que tous les participants sont déjà enregistrés.")
    while questionary.confirm(
                             "Voulez-vous selectionner un joueur? Y/N"
                             ).ask():
        list_registered_player.append(
            questionary.select(
                               "Sélectionnez le joueur à \
                                ajouter à la liste de suppression",
                               choices=get_every_players_in_db()).ask()
            )
        print("Vous allez ajouter :")
        print(list_registered_player)
    return list_registered_player


def ask_who_to_remove():
    remove_players(select_players_in_DB())
    return "Gestion des utilisateurs"

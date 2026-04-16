import questionary
from datetime import datetime

import constants
from models.DB_manager import (
    save_in_database,
    save_tournament_update,
    get_list_tournaments_in_db,
    get_instances_from_DB
)
from controls.player import (
    input_player,
    get_every_players_in_db,
    format_player_list
)
from controls.reports import create_report
from controls.tournament import (
    input_tournament,
    check_max_number_of_round,
    generate_round,
    format_tournament,
    format_historic
)

from views.menu import display_main_menu, \
                          display_player_menu, \
                          display_tournament_menu, \
                          display_report_menu
from views.player import ask_who_to_remove
from views.tournament import sign_up_players


def main_menu():
    navigate_through_main_menu = display_main_menu()
    while navigate_through_main_menu != constants.EXIT:
        match navigate_through_main_menu:
            case constants.PLAYER_MENU:
                navigate_through_main_menu = execute_player_menu()
            case constants.TOURNAMENT_MENU:
                navigate_through_main_menu = execute_tournament_menu()
            case constants.REPORT_MENU:
                navigate_through_main_menu = execute_report_menu()
            case constants.SAVE_MENU:
                pass
            case constants.EXIT:
                pass
        navigate_through_main_menu = display_main_menu()
    return


def execute_player_menu():
    navigate_player_menu = display_player_menu()
    while navigate_player_menu != constants.RETURN_TO_MAIN:
        match navigate_player_menu:
            case "Ajouter un utilisateur":
                player_list = []
                while questionary.confirm(
                                        "Voulez-vous ajouter un joueur?"
                                        ).ask():
                    player_to_add = input_player()
                    player_list.append(player_to_add)
                    print("Saisie ok, avant sauvegarde ...")
                save_in_database(player_list, "player")
                print("Le(s) joueur(s) ont été ajouté à la base de donnée.")
            case "Supprimer un ou des joueurs":
                navigate_player_menu = ask_who_to_remove()
        navigate_player_menu = display_player_menu()
    return navigate_player_menu


def execute_tournament_menu():
    navigate_tournament_menu = display_tournament_menu()
    while navigate_tournament_menu != constants.RETURN_TO_MAIN:
        match navigate_tournament_menu:
            case "Ajouter un tournoi":
                print("Attention un seul tournoi peut être en cours!")
                tournament_to_create = input_tournament()
                print("Saisie ok, sauvegarde en cours...")
                save_in_database(tournament_to_create, "tournament")
            case "Ajouter des joueurs au tournoi":
                print("Assurez-vous que tous les participants"
                      "sont déjà enregistrés.")
                if questionary.confirm("Voulez-vous ajouter des participants"
                                       " à un tournoi?").ask():
                    selected_tournament = questionary.select(
                                    "A quel tournoi souhaitez-vous "
                                    "ajouter des joueurs ?",
                                    choices=get_list_tournaments_in_db()).ask()
                    players_list = get_every_players_in_db()
                    players_to_add = sign_up_players(players_list)
                    print("Les joueurs vont être chargés dans le tournoi")
                    save_tournament_update(selected_tournament,
                                           players_to_add,
                                           "player_to_register")
            case "Démarrer un Round":
                if questionary.confirm("Voulez-vous démarrer"
                                       " un nouveau round?").ask():
                    selected_tournament = questionary.select(
                                    "A quel tournoi souhaitez-vous "
                                    "ajouter un round ?",
                                    choices=get_list_tournaments_in_db()).ask()
                    loaded_tournament = get_instances_from_DB(
                        selected_tournament,
                        "tournament"
                        )
                    for elt in loaded_tournament:
                        if check_max_number_of_round(elt):
                            generate_round(elt)
                            save_tournament_update(
                                elt.__dict__["name"],
                                elt.__dict__["round_list"],
                                "match")
                        if not check_max_number_of_round(elt):
                            now = datetime.now()
                            elt.ending_date = now.strftime(
                                "%d/%m/%Y, %H:%M"
                                )
                            save_tournament_update(
                                elt.__dict__["name"],
                                elt.__dict__["ending_date"],
                                "ending"
                            )
        navigate_tournament_menu = display_tournament_menu()
    return navigate_tournament_menu


def execute_report_menu():
    navigate_report_menu = display_report_menu()
    separator = "\n"
    while navigate_report_menu != constants.RETURN_TO_MAIN:
        content = ""
        report_name = ""
        match navigate_report_menu:

            case "Joueurs par ordre alphabétique":
                imported_players = get_every_players_in_db()
                list_of_player_instances = get_instances_from_DB(
                    imported_players,
                    "player"
                    )
                sorted_list_of_player_instances = sorted(
                    list_of_player_instances,
                    key=lambda player: player.name
                    )
                sorted_player = format_player_list(
                    sorted_list_of_player_instances
                    )

                content = separator.join(sorted_player)
                report_name = constants.NAME_REPORT_PLAYER

            case "Tous les tournois":
                imported_tournaments = get_list_tournaments_in_db()
                list_of_tournament_instances = get_instances_from_DB(
                    imported_tournaments,
                    "tournament"
                    )
                for tournament in list_of_tournament_instances:
                    content = content + format_tournament(tournament)
                report_name = constants.NAME_REPORT_ALL_TOURNAMENT

            case "Nom et date du tournoi":
                selected_tournament = questionary.select(
                                    "Quel tournoi souhaitez_vous afficher?",
                                    choices=get_list_tournaments_in_db()).ask()
                loaded_tournament = get_instances_from_DB(
                    selected_tournament,
                    "tournament"
                    )
                for tournament in loaded_tournament:
                    content = (content
                               + tournament.name + "\n"
                               + tournament.beginning_date + "\n"
                               + tournament.ending_date + "\n")
                report_name = constants.NAME_REPORT_TOURNAMENT_NAME_AND_DATE

            case "Joueurs dans le tournoi":
                selected_tournament = questionary.select(
                                    "Quel tournoi souhaitez_vous afficher?",
                                    choices=get_list_tournaments_in_db()).ask()
                loaded_tournament = get_instances_from_DB(
                    selected_tournament,
                    "tournament"
                    )
                for tournament in loaded_tournament:
                    list_of_registered_players = (
                        tournament.registered_players_in_tournament_list
                        )
                    list_of_instance = get_instances_from_DB(
                        list_of_registered_players,
                        "player"
                        )
                    sorted_list_of_player_instances = list(
                        sorted(list_of_instance,
                               key=lambda player: player.name)
                        )
                    sorted_player = format_player_list(
                        sorted_list_of_player_instances
                        )
                    content = separator.join(sorted_player)

                report_name = (
                    constants.NAME_REPORT_PLAYERS_IN_TOURNAMENT
                    )

            case "Historique des matchs du tournoi":
                selected_tournament = questionary.select(
                                    "Quel tournoi souhaitez_vous afficher?",
                                    choices=get_list_tournaments_in_db()).ask()
                loaded_tournament = get_instances_from_DB(
                    selected_tournament,
                    "tournament"
                    )
                for tournament in loaded_tournament:
                    content = separator.join(format_historic(tournament))
                report_name = (
                    constants.NAME_REPORT_TOURNAMENT_ROUND_HISTORIC
                    )

        create_report(report_name, content)
        navigate_report_menu = display_report_menu()
    return navigate_report_menu

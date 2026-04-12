import questionary
import re
from typing import List
from tinydb import TinyDB, \
                   Query


import Constants
import Controls.C_validators
from Models.M_player import Player
from Views.V_menu import ask_which_attr_to_modify, ask_modification_value

db_player = TinyDB(Constants.PATH_TO_DB + Constants.PLAYER_DB_SUFFIX)


def input_player():
    player_to_instanciate = Player(
        input_name(),
        input_firstname(),
        input_birthdate(),
        input_national_id(),
        input_score()
    )
    return player_to_instanciate


@Controls.C_validators.validate_name
def input_name(): return questionary.text("Quel est le name du joueur?").ask()


@Controls.C_validators.validate_firstname
def input_firstname(): return questionary.text(
            "Quel est le firstname du joueur?"
            ).ask()


@Controls.C_validators.validate_date
def input_birthdate(): return questionary.text(
    "Quand le joueur est-il né?(Tapez au format : JJ/MM/AAAA)").ask()


@Controls.C_validators.validate_player_ID
def input_national_id(): return questionary.text(
    "Quel est l'identifiant national du joueur ?").ask()


def input_score():
    try:
        return int(questionary.text("Quel score le joueur possède-t-il").ask())
    except Exception:
        print("Vous n'avez pas saisie un nombre entier.")
        return input_score()


def modify_player():
    Player = Query()
    ask_modification = True
    while ask_modification:
        who_to_modifiy = questionary.text(
                                       '''
                                       Quel est l'identifiant national du
                                       joueur à modifier?
                                       '''
                                       ).ask()
        what_to_modify = []
        autreModif = True
        while autreModif:
            what_to_modify.append(
                input_modif_to_player(who_to_modifiy))
            autreModif = questionary.confirm(
                                            '''
                                            Souhaitez-vous apporter
                                            une autre modification au joueur?
                                            '''
                                            ).ask()
        # Couper la fonction à ce niveau
        for modif in what_to_modify:
            db_player.update({modif[0]: modif[1]},
                             Player.national_player_id == who_to_modifiy)
        # jusqu'ici
        ask_modification = questionary.confirm(
            "Voulez-vous modifier un autre joueur?").ask()
    return


def input_modif_to_player(who_is_modified):
    dummyinstance = Player("", "", "", "XX00000", "")
    what_to_modify = ask_which_attr_to_modify(dummyinstance.__dict__.keys())
    replace_by = ask_modification_value(what_to_modify, who_is_modified)
    return (what_to_modify, replace_by)


def append_player_to_list(players_list, player):
    listetemp = []
    listetemp = players_list
    listetemp.append(player)
    return listetemp


def format_player_list(list_of_player_instances: List[Player]) -> List:
    formated_list = []
    for player in list_of_player_instances:
        if type(player) is Player:
            player_id = (player.name
                         + " "
                         + player.firstname
                         + ", "
                         + player.national_player_id
                         )
        else:
            player_id = (player["name"]
                         + " "
                         + player["firstname"]
                         + ", "
                         + player["national_player_id"]
                         )
        formated_list.append(player_id)
    return formated_list


def format_player(load_player):
    def wrapper():
        try:
            player_list = load_player()
        except Exception:
            print("Player list can't be loaded.")
            return wrapper()
        return format_player_list(player_list)
    return wrapper


# TODO : move get every players in db to DB manager
@format_player
def get_every_players_in_db():
    db_player.clear_cache()
    player = Query()
    loaded_list = db_player.search(player.name != None) # noqa : E711
    return loaded_list


def remove_players(player_list):
    register = Query()
    for name in player_list:
        m = re.match(r"(?P<name>\w+) (?P<firstname>\w+)", name)
        name_of_players_to_remove = m.group('name')
        try:
            db_player.remove(register.name.search(name_of_players_to_remove))
            print(f"{name} a été supprimé(e)")
        except Exception:
            print(f"{name} n'a pas pu être supprimé(e)")
    return


def load_wanted_players(formated_player_list: List[str]) -> List[Player]:
    request = Query()
    player_list = []
    for elt in formated_player_list:
        searched_player = db_player.search(
            request.national_player_id
            == elt[-7:])
        joueur = Player(searched_player[0]["name"],
                        searched_player[0]["firstname"],
                        searched_player[0]["birthdate"],
                        searched_player[0]["national_player_id"],
                        searched_player[0]["current_score"]
                        )
        player_list.append(joueur)
    return player_list


def sort_player(playerList: List[Player]):
    temporary_list = []
    sorted_player_list = []
    for player in playerList:
        temporary_list.append((player.name, player))

    temporary_list.sort()
    for key, player in temporary_list:
        sorted_player_list.append(player)
        return sorted_player_list


def get_player_as_list(player: Player):
    player_as_list = []
    for key, value in player.__dict__:
        player_as_list.append(value)
    return player_as_list

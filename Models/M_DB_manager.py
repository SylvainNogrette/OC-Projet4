from tinydb import (
    TinyDB,
    Query
)
from copy import deepcopy

import Models.M_player
import Models.M_tournament


PATH_TO_DB = 'Base_de_données'
DB_TOURNAMENT = TinyDB(PATH_TO_DB + '/tournois.json')
DB_PLAYER = TinyDB(PATH_TO_DB + '/joueurs.json')


def save_in_database(registration, in_which_db):
    '''
    Docstring for save_in_database
    :param registration: object to register in database
    :param in_which_db: which type of data is registered
    '''
    if in_which_db == "tournament":
        if not id_is_in_db(registration.name, "tournament"):
            DB_TOURNAMENT.insert(registration.__dict__)
        else:
            print("Ce tournoi existe déjà.")
    elif in_which_db == "player":
        for player in registration:
            DB_PLAYER.insert(player.__dict__)
    else:
        print("Aucune base de données ne "
              "correspond au type choisi")
        return
    print("Sauvegarde dans la base de données effectuée")
    return


def save_tournament_update(what_to_update: str,
                           what_to_register: list,
                           type_of_update: str):
    '''
    Docstring for load_tournament_players
    Overwrite registered_players_in_tournament_list
    by players_to_register in database
    :param what_to_update: name of the tournament
                                 user intends to add players to
    :type what_to_update: str
    :param what_to_register: list of str
    :type what_to_register: List[str]
    :param type_of_update: Category of attr to update in tournament db
    :type type_of_update: str
    '''
    query = Query()

    if type_of_update == "player_to_register":
        DB_TOURNAMENT.update(
            {"registered_players_in_tournament_list": what_to_register},
            query.name.search(what_to_update))

    if type_of_update == "match":
        tournament_to_update = deepcopy(DB_TOURNAMENT.search(
            query.name == what_to_update
            ))
        for tournament in tournament_to_update:
            number_of_round = tournament["current_round_number"] + 1
            search = query.name.search(what_to_update)
            update_to_do = [
                {"round_list": what_to_register},
                search,
                {"current_round_number": number_of_round},
                search
            ]
            for update in update_to_do:
                DB_TOURNAMENT.update(update)
        return
    if type_of_update == "ending":
        search = query.name.search(what_to_update)
        DB_TOURNAMENT.update({"ending_date": what_to_register})

    if type_of_update == "score":
        DB_PLAYER.update(
            {"current_score": what_to_register},
            query.national_player_id.search(what_to_update)
        )
    return


def get_list_tournaments_in_db():
    '''
    Docstring for get_list_tournaments_in_db
    Return list of all tournaments name in database
    '''
    try:
        tournament = Query()
        list_tournaments = []
        list_tournaments_to_browse = deepcopy(DB_TOURNAMENT.all())
        for tournaments_from_db in list_tournaments_to_browse:
            resultatRecherche = []
            resultatRecherche.append(
                DB_TOURNAMENT.search(
                    tournament.name == tournaments_from_db["name"]))
            idTournoi = tournaments_from_db["name"]
            list_tournaments.append(idTournoi)
    except Exception:
        print("Aucun tournoi n'est enregistré.")
        return
    return list_tournaments


def get_instances_from_DB(id_list, type_of_object):
    '''Return list of chosen instances from database.'''
    request = Query()
    instance_list = []
    if type_of_object == "player":
        for elt in id_list:
            searched_player = DB_PLAYER.search(
                request.national_player_id
                == str(elt)[-7:])
            player = Models.M_player.Player(
                            searched_player[0]["name"],
                            searched_player[0]["firstname"],
                            searched_player[0]["birthdate"],
                            searched_player[0]["national_player_id"],
                            searched_player[0]["current_score"]
                            )
            instance_list.append(player)
        return instance_list
    elif type_of_object == "tournament":
        if type(id_list) is not list:
            id = []
            id.append(id_list)
        else:
            id = id_list
        for tournament in id:
            searched_tournament = DB_TOURNAMENT.search(
                request.name == tournament
            )
            tournament = Models.M_tournament.Tournament(
                searched_tournament[0]["name"],
                searched_tournament[0]["place"],
                searched_tournament[0]["beginning_date"],
                searched_tournament[0]["ending_date"],
                searched_tournament[0]["current_round_number"],
                searched_tournament[0]["round_list"],
                get_instances_from_DB(
                    (searched_tournament[0]
                     ["registered_players_in_tournament_list"]
                     ),
                    "player"
                    ),
                searched_tournament[0]["description"],
                searched_tournament[0]["number_of_round"]
            )
            instance_list.append(tournament)
        return instance_list
    else:
        print("Le type de donnée ne correspond à aucune base de données")
        return


def id_is_in_db(id, type):
    if type == "player":
        player = Query()
        if DB_PLAYER.search(player.national_player_id == id) != []:
            return True
        else:
            return False
    elif type == "tournament":
        tournament = Query()
        if DB_TOURNAMENT.search(tournament.name == id) != []:
            return True
        else:
            return False
    else:
        print("Ce type de base de données n'existe pas.")


def get_all_docs_from_db(db_type: str) -> list:
    '''Return list of all docs from database'''
    if db_type == "player":
        return DB_PLAYER.all()
    elif db_type == "tournament":
        return DB_TOURNAMENT.all()
    else:
        print(f"Le type {db_type} ne correspond à aucune base de données.")

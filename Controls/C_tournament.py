from typing import List, Tuple
from random import shuffle
from datetime import datetime
from copy import deepcopy


from tinydb import TinyDB


from Models.M_tournament import Tournament
from Models.M_round import Round
from Models.M_DB_manager import save_tournament_update

from Views.V_tournament import input_tournament_name, \
                             input_tournament_place, \
                             input_number_of_round, \
                             input_tournament_description, \
                             ask_outcome_of_match


PATH_TO_DB = 'Base_de_données'
DB_TOURNAMENT = TinyDB(PATH_TO_DB + '/tournois.json')


def input_tournament():
    now = datetime.now()
    tournament_to_create = Tournament(
        input_tournament_name(),
        input_tournament_place(),
        now.strftime("%d/%m/%Y, %H:%M"),
        "",
        0,
        [],
        [],
        input_tournament_description(),
        input_number_of_round()
        )
    return tournament_to_create


def get_historic_without_score(historic: list[list]) -> list[set]:
    historic_without_score = []
    for match in historic:
        match_without_score = set()
        for opponent in match:
            match_without_score.add(opponent[0])
        historic_without_score.append(match_without_score)
    return historic_without_score


def correct_sorted_players_by_match_historic(tournament: Tournament):
    '''
    From sorted list by score. Take one player then find the next best
    player who hasn't played with yet. This player is placed right
    after the player in the list.
    '''
    historic = get_list_of_every_match(tournament)
    historic_without_score = get_historic_without_score(historic)
    sorted_players = []
    temp_registered_players_in_tournament_list = deepcopy(
        tournament.registered_players_in_tournament_list
        )
    number_of_dual = int(
        len(tournament.registered_players_in_tournament_list)
        / 2
        )
    for i in range(number_of_dual):

        first_player = temp_registered_players_in_tournament_list[0]

        # iterate on the player list minus every player until firstplayer index
        it_second_player = iter(
                temp_registered_players_in_tournament_list[1:]
                )
        second_player = next(it_second_player)
        match_combinations = {str(first_player), str(second_player)}
        # set of two players to check if the match is in historic of matches
        all_matchup_already_played = False
        while match_combinations in historic_without_score:
            try:
                second_player = next(it_second_player)
                match_combinations = {str(first_player), str(second_player)}
            except StopIteration:
                all_matchup_already_played = True
                break
        if all_matchup_already_played:
            # if all matchup has been played, keep the score sorting order
            second_player = temp_registered_players_in_tournament_list[1]

        sorted_players.extend([first_player, second_player])
        temp_registered_players_in_tournament_list.remove(second_player)
        temp_registered_players_in_tournament_list.remove(first_player)

    tournament.registered_players_in_tournament_list.clear()
    tournament.registered_players_in_tournament_list.extend(sorted_players)
    return


def generate_next_list_of_matches(
        sorted_player_list: List) -> List[Tuple]:
    '''
   Pairs each two element in a tuple and return list of pairs
    '''
    list_of_new_matches = []
    temp_sorted_player_list = sorted_player_list
    while len(temp_sorted_player_list) > 1:
        list_of_new_matches.append(
            (temp_sorted_player_list[0],
             temp_sorted_player_list[1])
                                )
        temp_sorted_player_list.pop(1)
        temp_sorted_player_list.pop(0)
    return list_of_new_matches


def check_max_number_of_round(checked_tournament: Tournament):
    '''Check if the maximum of rounds in tournament has already been created'''

    round_number = checked_tournament.__dict__["current_round_number"]
    max_number_of_round = checked_tournament.__dict__["number_of_round"]
    if int(round_number) >= int(max_number_of_round):
        print("Tous les rounds du tournoi ont déjà été crée")
        return False
    else:
        print("Un round supplémentaire peut bien être créer.")
        return True


def generate_round(tournament: Tournament):

    tournament.current_round_number = len(tournament.round_list)
    # generate the player list
    if tournament.get_current_round_number() == 0:
        for player in tournament.registered_players_in_tournament_list:
            player.reset_score()
        sorted_player_list = \
            tournament.format_registered_players()
        shuffle(sorted_player_list)
    else:
        sort_players_by_score(tournament)
        correct_sorted_players_by_match_historic(tournament)
        sorted_player_list = tournament.format_registered_players()

    tournament.current_round_number += 1
    now = datetime.now()
    beginning_date = now.strftime("%d/%m/%Y")

    round_to_generate = Round(
        define_name_of_next_round(tournament),
        beginning_date,
        "",
        []
        )
    round_to_generate.generate_round_matches(
        generate_next_list_of_matches(
            set_outcome_of_matches(tournament))
    )
    now = datetime.now()
    round_to_generate.dateFin = now.strftime("%d/%m/%Y")
    tournament.round_list.append(round_to_generate.get_serializable_round())
    return


def set_outcome_of_matches(tournament: Tournament):
    list_of_match_composition = []
    player_instance_list = deepcopy(
        tournament.registered_players_in_tournament_list
        )
    index_player = 0
    while index_player < len(player_instance_list)-1:
        index_player2 = index_player + 1
        player1 = player_instance_list[index_player]
        player2 = player_instance_list[index_player2]
        winner = ask_outcome_of_match(
            str(player_instance_list[index_player]),
            str(player_instance_list[index_player2])
        )

        if winner == str(player1):
            player1_match_result = 1
            player2_match_result = 0

        elif winner == str(player2):
            player1_match_result = 0
            player2_match_result = 1

        else:
            player1_match_result = 0.5
            player2_match_result = 0.5

        player1.modify_score(player1_match_result)
        player2.modify_score(player2_match_result)

        save_tournament_update(
            str(player1.national_player_id),
            player1.current_score,
            "score")
        save_tournament_update(
            str(player2.national_player_id),
            player2.current_score,
            "score")

        current_match_data = (
            [str(player1), player1_match_result],
            [str(player2), player2_match_result]
        )

        list_of_match_composition.append(current_match_data)
        index_player += 2
#        player_instance_list.pop(1)
#        player_instance_list.pop(0)
    tournament.registered_players_in_tournament_list = player_instance_list
    return list_of_match_composition

# TODO : validate registered players are in even number


def define_name_of_next_round(tournament: Tournament):
    return str("Round " + str(tournament.get_current_round_number()))


def get_list_of_every_match(tournament: Tournament) -> List[dict]:
    '''Returns list of every past matches in the tournament'''
    list_of_every_matches = []
    list_of_rounds = tournament.__dict__["round_list"]
    for round in list_of_rounds:
        list_of_matches_in_round = round["match_list"]
        for match in list_of_matches_in_round:
            list_of_every_matches.extend(match)
    return list_of_every_matches


def list_every_individual_result(list_of_every_matches: List[Tuple[List]]):
    list_of_individual_result = []
    for match in list_of_every_matches:
        for individual_result in match:
            list_of_individual_result.append(individual_result)
    return list_of_individual_result


def get_every_global_result_in_tournament(
        list_of_players: List,
        every_individual_result: List[List]):
    '''
    Return a list of tuple with both player
    and global result at the tournament.
    :param list_of_players: List of player
    formated as str "name firstname, nationalID"
    :type list_of_players: List
    :param every_individual_result: List[List]
    '''
    list_of_global_result = []
    for player in list_of_players:
        player_score_in_tournament = 0
        for individual_result in every_individual_result:
            if player == individual_result["matchup_and_outcome"][0]:
                player_score_in_tournament += (
                    individual_result["matchup_and_outcome"][1]
                    )
        player_global_result = (player, player_score_in_tournament)
        list_of_global_result.append(player_global_result)
    return list_of_global_result


def sort_players_by_score(tournament: Tournament):
    tournament.registered_players_in_tournament_list.sort(
        key=lambda x: x.current_score,
        reverse=True
        )


def format_historic(tournament: Tournament) -> list:
    historic_as_list = []
    historic_as_list.append("Tournoi : " + tournament.name)

    for round in tournament.round_list:
        historic_as_list.append("\n ID du Round : " + round["round_id"])
        historic_as_list.append("\n Liste des matchs :")
        for match in round["match_list"][0]:
            historic_as_list.append(str(match))
    return historic_as_list


def format_tournament(tournament: Tournament) -> str:
    round_as_text = ""
    for round in tournament.round_list:
        round_as_text = (round_as_text
                         + "\nID du Round : \n"
                         + round["round_id"]
                         )
        round_as_text = round_as_text + "\nListe des matchs : \n"
        for match in round["match_list"][0]:
            round_as_text = round_as_text + str(match) + "\n"
        round_as_text = (round_as_text
                         + "Date de début : \n"
                         + round["dateDebut"]
                         )
        round_as_text = (round_as_text
                         + "Date de fin : \n"
                         + round["dateFin"]
                         )
    tournament_as_list = [
        "Nom :\n",
        tournament.name,
        "\nLieu :\n",
        tournament.place,
        "\nDate de début :\n",
        tournament.beginning_date,
        "\nDate de fin :\n",
        tournament.ending_date,
        "\nNombre de rounds :\n",
        str(tournament.number_of_round),
        "\nRound en cours :\n",
        str(tournament.current_round_number),
        "\nListe des rounds :",
        round_as_text,
        "\nListe des joueurs inscrits :\n",
        "\n".join(tournament.format_registered_players()),
        "\n\n\n"
    ]
    tournament_as_text = "".join(tournament_as_list)
    return tournament_as_text

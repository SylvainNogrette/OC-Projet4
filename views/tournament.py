import questionary
from tinydb import TinyDB
from typing import List


from controls.validators import validate_date_plus_hour


path_to_db = 'Base_de_données'
tournament_db = TinyDB(path_to_db + '/tournois.json')


def input_tournament_name():
    return questionary.text("Quel est le name du tournoi?").ask()


def input_tournament_place():
    return questionary.text("Où se déroule le tournoi?").ask()


@validate_date_plus_hour
def input_tournament_beginning():
    return questionary.text("Donnez la date et l'heure de "
                            "début du tournoi au format JJ/MM/AAAA, "
                            "HH:mm").ask()


@validate_date_plus_hour
def input_tournament_ending():
    return questionary.text(
        "Donnez la date et l'heure de fin du"
        "tournoi au format JJ/MM/AAAA, HH:mm"
    ).ask()


@validate_date_plus_hour
def input_round_beginning():
    return questionary.text("Donnez la date et l'heure de début du round "
                            "au format JJ/MM/AAAA, HH:mm"
                            ).ask()


@validate_date_plus_hour
def input_round_ending():
    return questionary.text("Donnez la date et l'heure de fin du round "
                            "au format JJ/MM/AAAA, HH:mm"
                            ).ask()


def input_number_of_round():
    result = questionary.text("Quel nombre de tours contient votre tournoi?").ask()
    if result:
        return result
    else:
        return "4"


def input_tournament_description():
    return questionary.text(
        "Ajoutez une description ou une remarque."
    ).ask()


def input_ending():
    return questionary.text(
        "Quelle est la date de fin du tournoi (JJ/MM/AAAA, hh:mm)"
        ).ask()


def sign_up_players(remaining_players_to_choose: List[str]) -> List[str]:

    signed_up_players = []
    while (
        remaining_players_to_choose
        and questionary.confirm("Voulez-vous ajouter un joueur? Y/N").ask()
    ):
        chosen_player = questionary.select(
            "Sélectionnez un joueur à ajouter au tournoi",
            choices=remaining_players_to_choose
        ).ask()

        signed_up_players.append(chosen_player)
        remaining_players_to_choose.remove(chosen_player)

    return signed_up_players


def ask_outcome_of_match(player1: str, player2: str) -> str:
    '''Ask and return the player who won the match and return it as String '''
    winner = questionary.select(
        "Parmi les joueurs du match, qui est sorti vainqueur?",
        choices=[player1, player2, "Personne"]
        ).ask()
    return winner

from models.match import Match


class Round():
    """
    Round is a list of matches played between two dates with an ID.
    param:
    match_list: list of matches
    round_id is the ID of the Round
    dateDebut is the beginning date
    dateFin is the ending date
    """
    def __init__(self, round_id: str, beginning_date_and_hour: str,
                 ending_date_and_hour='', match_list=[]):
        self.round_id = round_id
        self.match_list = match_list
        self.dateDebut = beginning_date_and_hour
        self.dateFin = ending_date_and_hour

    def generate_round_matches(self, list_of_match_composition):
        for match_composition in list_of_match_composition:
            match = Match(match_composition)
            self.match_list.append(match.__dict__["matchup_and_outcome"])
            list_of_match_composition.pop(0)
        return

    def get_round_name(self):
        return self.round_id

    def get_serializable_round(self):

        dict_to_return = {
            "round_id": self.round_id,
            "match_list": self.match_list,
            "dateDebut": self.dateDebut,
            "dateFin": self.dateFin
        }
        return dict_to_return

class Tournament():
    '''
    Contains data about a tournament and several methods
    to access it or set value to its attributes
    '''
    def __init__(self, name, place, beginning_date, ending_date,
                 current_round_number, round_list,
                 registered_players_in_tournament_list,
                 description, number_of_round=4):
        self.name = name
        self.place = place
        self.beginning_date = beginning_date
        self.ending_date = ending_date
        self.number_of_round = number_of_round
        self.current_round_number = current_round_number
        self.round_list = round_list
        self.registered_players_in_tournament_list = (
            registered_players_in_tournament_list
        )
        self.description = description

    def get_round_list(self):
        list_of_round_dict = []
        for round in self.round_list:
            list_of_round_dict.append(round)
        return list_of_round_dict

    def get_current_round_number(self):
        return self.current_round_number

    def format_registered_players(self):
        formated_list_registered_players = []
        for player in self.registered_players_in_tournament_list:
            formated_list_registered_players.append(player.__str__())
        return formated_list_registered_players

    def get_serializable_tournament(self):
        round_list = []
        for round in self.round_list:
            round_list.append(round)
        dict_to_return = {
            "name": self.name,
            "place": self.place,
            "beginning_date": self.beginning_date,
            "ending_date": self.ending_date,
            "number_of_round": self.number_of_round,
            "current_round_number": self.current_round_number,
            "round_list": round_list,
            "registered_players_in_tournament_list":
            self.format_registered_players()
        }
        return dict_to_return

    def get_number_of_registered_player(self):
        return len(self.registered_players_in_tournament_list)

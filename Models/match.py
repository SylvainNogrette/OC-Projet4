class Match():
    """
    param : tupple containing 2 lists with each player and his score
    """
    def __init__(self, matchup_and_outcome=([], [])):
        self.matchup_and_outcome = matchup_and_outcome

    def get_player_score(self, player_name):
        for player in self.matchup_and_outcome:
            if player_name == player[0]:
                print(player[1])
                return player[1]
        return

    def display_ID_Match(self):
        strmatch = (
            self.matchup_and_outcome[0][0]
            + "/"
            + self.matchup_and_outcome[1][0]
            )
        print(strmatch)
        return

    def is_finished(self):
        if (
            self.matchup_and_outcome[0][1]
            + self.matchup_and_outcome[1][1] == 1
        ):
            return True
        else:
            return False

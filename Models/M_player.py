class Player ():
    """
    La classe Joueur contient les informations relatives au joueur et
    notamment son identifiant National unique ainsi que son score.
    """

    def __init__(self, name: str, firstname: str, birthdate: str,
                 national_player_id: str, current_score: int):
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.national_player_id = national_player_id
        self.current_score = current_score

    def __str__(self):
        '''
        Permet l'affichage d'une string identifiant un joueur
        avec son name, firstname et identifiant national
        '''
        player_id_display = "{} {}, {}".format(
            self.name,
            self.firstname,
            self.national_player_id
            )
        return player_id_display

    def get_IDnat(self):
        return self.national_player_id

    def modify_score(self, added_score: int):
        self.current_score += added_score
        return

    def reset_score(self):
        self.current_score = 0
        return

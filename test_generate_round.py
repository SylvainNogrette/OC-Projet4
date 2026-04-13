from Controls.C_tournament import generate_round
import Models.M_tournament
import Models.M_player


player1 = Models.M_player.Player(
    "Peuplu",
    "Jean",
    "05/05/1995",
    "AR54632",
    0.5
)
player2 = Models.M_player.Player(
    "Danlédoi",
    "Léanor",
    "03/03/1995",
    "AP54632",
    0.5
)
player3 = Models.M_player.Player(
    "Euldaibu",
    "Luc",
    "04/03/1980",
    "IP54632",
    1
)
player4 = Models.M_player.Player(
    "Adhi",
    "Jacques",
    "03/12/1995",
    "UC54632",
    0
)
tournament = Models.M_tournament.Tournament(
    "Tournoi_test_1",
    "Bureau",
    "19/03/2026, 20:00",
    "19/03/2026, 21:00",
    1,
    [
        {
            "round_id": "Round 1",
            "match_list": [
                [
                    [
                        [
                            "Euldaibu Luc, IP54632",
                            1
                        ],
                        [
                            "Adhi Jacques, UC54632",
                            0
                        ]
                    ],
                    [
                        [
                            "Danlédoi Léanor, AP54632",
                            0.5
                        ],
                        [
                            "Peuplu Jean, AR54632",
                            0.5
                        ]
                    ]
                ]
            ],
            "dateDebut": "27/03/2026, 10:00",
            "dateFin": "27/03/2026, 10:00"
        }
    ],
    [
     player1,
     player2,
     player3,
     player4
     ],
    "RAS",
    3
)
""" sort_players_by_score(tournament)
correct_sorted_players_by_match_historic(tournament)
print("Tri attendu :")
print(f"{player3}{player2}, {player4}{player1} ou")
print(f"{player3}{player1}, {player2}{player4}")
print("Joueurs après tri :")
for player in tournament.registered_players_in_tournament_list:
    print(player) """
generate_round(tournament)
generate_round(tournament)
generate_round(tournament)
for round in tournament.round_list:
    print(round)
for player in tournament.registered_players_in_tournament_list:
    print(f"{str(player)}, {player.current_score}")

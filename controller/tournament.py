from controller.player import create_player, update_rankings
from controller.database import save_db, update_db, load_player, load_tournament
from models.tournament import Tournament
# from views.main_menu import MainMenu
from views.player import LoadPlayer
from views.view import View
from views.tournament import CreateTournament, LoadTournament

# def display_main_menu


def create_tournament():

    menu = View()
    # Récupération des infos du tournoi
    user_entries = CreateTournament().display_menu()

    # Choix chargement joueurs:
    print("-"*50)
    user_input = menu.get_user_entry(
        message_display="1 - Créer des joueurs\n2 - Charger des joueurs\n Votre choix :",
        message_error="Entrez un choix valide.",
        input_value="select",
        statement=["1","2"]
    )

    # Chargement des joueurs
    if user_input == "2":
        players = []
        user_input = menu.get_user_entry(
            message_display="Charger combien de joueurs ?\n",
            message_error="Entrez 0 ou 1.",
            input_value="int"
        )
        serialized_players = LoadPlayer().display_menu(
            nb_players_to_load=user_input
        )
        for serialized_player in serialized_players:
            player = load_player(serialized_player)
            players.append(player)

    # Creation des joueurs
    else:
        print(f"\nCréation de {str(user_entries['nb_players'])} joueurs.")
        players = []
        while len(players) < user_entries['nb_players']:
            players.append(create_player())

    # Creation du tournoi
    tournament = Tournament(
        user_entries['name'],
        user_entries['location'],
        user_entries['date'],
        user_entries['time_control'],
        players,
        user_entries['nb_rounds'],
        user_entries['description'])

    # Save du tournoi dans la bdd
    save_db("tournaments", tournament.get_serialized_tournament())

    return tournament


def play_tournament(tournament, new_tournament_loaded=False):

    menu = View()
    print("-"*50)
    print(f"Début du tournoi {tournament.name}")
    print("-"*50)

    while True:

        # Si nouveau tournoi chargé: Calcul des rounds restants à jouer
        a = 0
        if new_tournament_loaded:
            for round in tournament.rounds:
                if round.end_date == "":
                    a += 1
            nb_rounds_to_play = tournament.nb_rounds - a
            new_tournament_loaded = False
        else:
            nb_rounds_to_play = tournament.nb_rounds

        for i in range(nb_rounds_to_play):

            # Création du round
            tournament.create_round(round_number=i+a)

            # On joue le dernier round créé
            current_round = tournament.rounds[-1]
            print()
            print(current_round.start_date + " : Début du " + current_round.name)

            # Round terminé, on passe au round suivant, on peux aussi mettre à jour les classements manuellement
            while True:
                print()
                user_input = menu.get_user_entry(
                    message_display="1 - Lancer le match \n"
                                "2 - Voir les classements\n"
                                "3 - Mettre à jour les classements\n"
                                "4 - Sauvegarder le tournoi\n"
                                "5 - Charger un tournoi\n"
                                "Votre choix : ",
                    message_error="Veuillez faire un choix.",
                    input_value="select",
                    statement=["1", "2", "3", "4","5"]
                )
                print("-"*50)

                # Round suivant
                if user_input == "1":
                    current_round.mark_as_complete()
                    break

                # Affichage des classements
                elif user_input == "2":
                    print(f"Classement du tournoi {tournament.name}\n:")
                    for i, player in enumerate(tournament.get_rankings()):
                        print(f"{str(i + 1)} - {player}")

                # Changement des rangs
                elif user_input == "3":
                    for player in tournament.players:
                        rank = menu.get_user_entry(
                            message_display=f"Rang de {player}:\n",
                            message_error="Veuillez entrer un nombre entier.",
                            input_value="int"
                        )
                        update_rankings(player, rank, score=False)

                # Sauvegarder le tournoi
                elif user_input == "4":
                    rankings = tournament.get_rankings()
                    for i, player in enumerate(rankings):
                        for t_player in tournament.players:
                            if player.name == t_player.name:
                                t_player.rank = str(i + 1)
                    update_db("tournaments", tournament.get_serialized_tournament(save_rounds=True))

                # Charger un tournoi
                elif user_input == "5":
                    serialized_loaded_tournament = LoadTournament().display_menu()
                    tournament = load_tournament(serialized_loaded_tournament)
                    new_tournament_loaded = True
                    break

            if new_tournament_loaded:
                break

        if new_tournament_loaded:
            continue

        else:
            break

    # Une fois le tournoi terminé, on le save dans la bdd puis on retourne les résultats
    rankings = tournament.get_rankings()
    for i, player in enumerate(rankings):
        for t_player in tournament.players:
            if player.name == t_player.name:
                t_player.total_score += player.tournament_score
                t_player.rank = str(i+1)
    update_db("tournaments", tournament.get_serialized_tournament(save_rounds=True))
    return rankings

from controller.database import load_tournament
from controller.player import update_rankings
from controller.tournament import create_tournament, play_tournament

from views.report import Report
from views.view import View
from views.tournament import LoadTournament

class MainMenu(View):

    def display_main_menu(self):

        while True:
            print("-"*20 + " MENU PRINCIPAL " + "-"*20)
            user_input = self.get_user_entry(
                message_display="[ 1 ]- Créer un tournoi\n"
                            "[ 2 ] - Reprendre un tournoi en cour \n"
                            "[ 3 ] - Voir les rapports\n"
                            "[ q ]- Quitter\n"
                            "Votre choix : ",
                message_error="Veuillez entrer une valeur valide",
                input_value="select",
                statement=[ "1", "2", "3","q"]
            )

            # Creer un tournoi
            if user_input == "1":
                tournament = create_tournament()
                break

            # Charger un tournoi
            elif user_input == "2":
                serialized_tournament = LoadTournament().display_menu()
                if serialized_tournament:
                    tournament = load_tournament(serialized_tournament)
                    break
                else:
                    print("Aucun tournoi sauvegardé !")
                    continue

            # Voir les rapports
            elif user_input == "3":
                while True:
                    user_input = self.get_user_entry(
                        message_display="1 - Joueurs\n2 - Tournois\nq - Retour au menu principal\n",
                        message_error="Veuillez faire un choix valide.",
                        input_value="select",
                        statement=["1", "2", "q"]
                    )

                    if user_input == "q":
                        break

                    elif user_input == "1":
                        while True:
                            user_input = self.get_user_entry(
                                message_display="Voir le classement :\n"
                                            "1 - Par rang\n"
                                            "2 - Par ordre alphabétique\n"
                                            "q - Retour au menu principal\n",
                                message_error="Veuillez faire un choix valide.",
                                input_value="select",
                                statement=[ "1", "2", "q"]
                            )
                            if user_input == "q":
                                break
                            elif user_input == "1":
                                sorted_players = Report().sort_players(Report().players, by_rank=True)
                                Report().display_players_report(players=sorted_players)
                            elif user_input == "2":
                                sorted_players = Report().sort_players(Report().players, by_rank=False)
                                Report().display_players_report(players=sorted_players)

                    elif user_input == "2":
                        Report().display_tournaments_reports()
            else:
                quit()

        # on joue le tournoi
        print()
        user_input = self.get_user_entry(
            message_display="1 - Jouer le tournoi\n"
                        "q - Quitter\n",
            message_error="Veuillez entrer une valeur valide",
            input_value="select",
            statement=["1", "q"]
        )

        # on récupère les résultats une fois le tournoi terminé
        if user_input == "1":
            rankings = play_tournament(tournament, new_tournament_loaded=True)
        else:
            quit()

        # on affiche les résultats
        print("-"*50)
        print(f"Tournoi {tournament.name} terminé !\nRésultats:")
        for i, player in enumerate(rankings):
            print(f"{str(i + 1)} - {player}")

        # on met à jour les classements
        print()
        user_input = self.get_user_entry(
            message_display="Mise à jour des classements\n"
                        "1 - Automatiquement\n"
                        "2 - Manuellement\n"
                        "q - Quitter\n",
            message_error="Veuillez entrer une valeur valide",
            input_value="select",
            statement=[ "1","2" "q"]
        )
        if user_input == "1":
            for i, player in enumerate(rankings):
                # print(player.name)
                update_rankings(player, i + 1)

        elif user_input == "2":
            for player in rankings:
                rank = self.get_user_entry(
                    message_display=f"Rang de {player}:\n",
                    message_error="Veuillez entrer un nombre entier.",
                    input_value="int"
                )
                update_rankings(player, rank)

        else:
            MainMenu().display_main_menu()

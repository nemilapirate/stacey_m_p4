from controller.database import load_db
from views.setting import Setting

class CreatePlayer(Setting):

    def display_menu(self):
        print("-"*20 + " Création d'un joueur " + "-"*20)
        name = input("Nom du joueur :\n")

        first_name = input("Prénom du joueur :\n")

        dateofbirth = self.get_user_entry(
            message_display="Date de naissance (JJ-MM-AAAA):\n",
            message_error="Veuillez entrer une date au format valide: format JJ-MM-AAAA",
            input_value="date"
        )

        gender = self.get_user_entry(
            message_display="Genre [ H ] ou  F ]:\n",
            message_error="Veuillez entrer H ou F",
            input_value="select",
            statement=["H", "h", "F", "f"]
        )

        rank = self.get_user_entry(
            message_display="Rang:\n",
            message_error="Veuillez entrer une valeur numérique valide.",
            input_value="int"
        )

        print(f"Le Joueur {name} {first_name} à été créé.")

        return {
            "name": name,
            "first_name": first_name,
            "dateofbirth": dateofbirth,
            "gender": gender,
            "total_score": 0,
            "rank": rank,
        }

# Chargement des joueurs depuis la base de données
class LoadPlayer(Setting):

    def display_menu(self, nb_players_to_load):

        all_players = load_db("players")
        serialized_loaded_players = []
        for i in range(nb_players_to_load):
            print(f"Plus que {str(nb_players_to_load - i)} joueurs à charger.")
            display_msg = "Choisir un joueur:\n"

            assertions = []
            for i, player in enumerate(all_players):
                display_msg = display_msg + f"{str(i+1)} - {player['first_name']} {player['name']}\n"
                assertions.append(str(i+1))

            user_input = int(self.get_user_entry(
                message_display=display_msg,
                message_error="Veuillez entrer un nombre entier.",
                input_value="select",
                statement=assertions
            ))
            if all_players[user_input-1] not in serialized_loaded_players:
                serialized_loaded_players.append(all_players[user_input-1])
            else:
                print("Joueur déjà chargé.")
                nb_players_to_load += 1

        return serialized_loaded_players
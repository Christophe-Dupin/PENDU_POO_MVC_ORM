from platform import system as system_name
from subprocess import call as system_call


class View:
    """Manage all the display of the app."""

    def clear_screen(self):
        """Manage clear terminal cross platform."""
        # Check wich os are on the user computer.
        command = "cls" if system_name().lower() == "windows" else "clear"
        system_call([command])

    def menu(self):
        """Display The menu of the app."""
        user_input = input(
            """Tapez:\n
        1:Se connecter \n
        2:Créer un compte \n
        3:Commencer une partie \n
        4:Reprendre une partie \n
        5:Quitter ?
        """
        )
        user_key = ["1", "2", "3", "4", "5"]
        # Check if the input of the user is in the list of choice
        if user_input not in user_key:
            print("Choisissez une des quatre possibilités")
            return self.menu()
        return user_input

    def select_level(self):
        """Choose a diffculty for the game."""
        user_input = input(
            """Choisissez votre niveau:\n
        1:Mot de 5 à 8 lettres \n
        2:Mot de 8 lettres et plus\n
        """
        )
        return user_input

    def create_user_name(self):
        user_input_name = input(
            """Quel est votre nom:\n
        """
        )
        return user_input_name

    def sign_in(self):
        user_input_name = input(
            """Votre nom d'utilisateur:\n
        """
        )
        return user_input_name

    def message_app(self, message):
        return print(message)

    def display_word(self, word):
        return print(word)
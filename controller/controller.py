import random

from database.database import db
from models.models import User
from repositories.repositories import UserRepository
from config import MESSAGE_APP, WORDS_LIST_5_8, WORDS_LIST_8_MORE


class Brain:
    """Class responsible of the intelligence of the programme."""

    def __init__(self, user_repository, view):
        """Init the Brain class and acces to the repository."""
        self.view = view
        self.user_repository = user_repository
        self.running = True
        self.authenticated = False
        self.chance = 0

    def display_menu(self):
        menu = self.view.menu()
        if menu == "1":
            self.view.sign_in()
            self.authenticated = True
        elif menu == "2":
            self.view.clear_screen()
            user_name = self.view.create_user_name()
            new_user = User(user_name)
            self.user_repository.create_user(new_user)
            self.authenticated = True
            self.view.message_app(MESSAGE_APP[0])
        elif menu == "3":
            self.view.clear_screen()
            if self.authenticated:
                level = self.view.select_level()
                if level == "1":
                    self.view.message_app(
                        "{} un mot entre 5 et 8 lettres".format(MESSAGE_APP[2])
                    )
                    word = random.choice(WORDS_LIST_5_8)
                    self.view.display_word(word)
                elif level == "2":
                    self.view.message_app(
                        "{} un mot de plus de 8 lettres".format(MESSAGE_APP[2])
                    )
            else:
                self.view.message_app(MESSAGE_APP[1])
        elif menu != "4":
            self.running = False
            exit()
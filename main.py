"""Main file to run app."""
from models.models import User
from repositories.repositories import UserRepository
from database.database import db
from view.view import View
from controller.controller import Brain
from models.models import User


class Game:
    def __init__(self):
        self.view = View()
        self.user_repository = UserRepository(db)
        self.brain = Brain(self.user_repository, self.view)
        self.chance = 0
    def run_app(self):
        """Launch the programme."""
        while self.brain.running:
            self.brain.display_menu()


if __name__ == "__main__":
    app = Game()
    app.run_app()

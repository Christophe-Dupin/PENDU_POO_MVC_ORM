"""All models for the applications."""
from repositories.repositories import UserRepository
from database.database import db


class User(UserRepository):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Word:
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word

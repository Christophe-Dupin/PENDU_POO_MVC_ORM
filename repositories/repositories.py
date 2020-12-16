"""Manage all the relationship with the db."""
from database.database import db


class UserRepository:
    """Allow to mange user model in the DB."""

    def __init__(self, db):
        self.db = db

    def create_user(self, user):

        self.db.query(
            """INSERT INTO user (name) VALUES (:name)""", name=user.name
        )
        return user

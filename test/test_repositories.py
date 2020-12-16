from models.models import User
from repositories.repositories import UserRepository
from database.database import db


def test_createUser_to_db():
    a = User(3, "vero", "souchon")
    repo = UserRepository(db)
    result = repo.create_user(a)
    assert result == a



from app.sessions.entities.sessions import Session
from tests.sessions.entities.create_sessions import create_game


def a_session():
    return SessionBuilder()


class SessionBuilder:
    def __init__(self):
        self.game = create_game()

    def with_game(self, game):
        self.game = game
        return self

    def build(self):
        return Session(self.game)

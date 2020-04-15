from app.games.models.game import Game


class RideTheBusGame(Game):
    type = 'Ride the bus'

    def __init__(self, deck):
        super().__init__(deck)
        self.dealer = None
        self.player = None

    # TODO : Valide dealer
    def set_dealer(self, name):
        self.dealer = super().add_player(name)
        self.players.append(self.dealer)

    # TODO : Valide add player
    def add_player(self, name):
        self.player = super().add_player(name)
        self.players.append(self.player)

    # TODO
    def draw(self):
        pass
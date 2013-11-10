__author__ = 'dimv36'


class GameStrategy:
    def __init__(self, player, strategy=None):
        self.player = player
        if strategy is None:
            self.strategy = []
        else:
            self.strategy = list(strategy)

    def add_strategy(self, element):
        if self.strategy.count(element) == 0:
            self.strategy.append(element)

    def __eq__(self, other):
        return self.player == other.player and all(self.strategy) == all(other.strategy)

    def __str__(self):
        return "Игрок {0}, стратегии: {1}".format(self.player, self.strategy)

    def __repr__(self):
        return self.__str__()

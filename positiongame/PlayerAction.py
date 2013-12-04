__author__ = 'dimv36'


class PlayerAction:
    def __init__(self, name, action, probability, position):
        self.name = str(name)
        self.action = action
        self.probability = float(probability)
        self.position = position

    def __str__(self):
        return "PlayerAction\n {0}, {1}, {2}".format(self.action,
                                                     self.probability,
                                                     self.position)

    def __repr__(self):
        return "{0}, {1}, {2}".format(self.action,
                                      self.probability,
                                      self.position)

    def __eq__(self, other):
        return self.action == other.action and self.probability == other.probability and self.position == other.position

    def __ne__(self, other):
        return not self.__eq__(other)
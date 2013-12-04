__author__ = 'dimv36'
from .enums import *


class TreePositionGameNode:
    def __init__(self, position_type, information_set, player_number, player_actions):
        self.position_type = position_type
        self.information_set = information_set
        self.player_number = player_number
        self.player_actions = list(player_actions)

    def __str__(self):
        return "TreePositionGameNode\n {0}, {1}, {2}, {3}".format(self.position_type,
                                                                  self.information_set,
                                                                  self.player_number,
                                                                  self.player_actions)

    def __repr__(self):
        return "{0}, {1}, {2}, {3}".format(self.position_type,
                                           self.information_set,
                                           self.player_number,
                                           self.player_actions)

    def __eq__(self, other):
        return self.position_type == other.position_type and self.information_set == other.information_set and \
            self.player_number == other.player_number and self.player_actions == other.player_actions

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_correct_behaviour(self):
        pass
        #TODO: реализовать метод
__author__ = 'dimv36'


class SrpGamersProbabilityDistribution:
    def __init__(self, first, second, price):
        self.first = first
        self.second = second
        self.game_price = price

    def __str__(self):
        first_length = len(self.first)
        second_length = len(self.second)
        output = "Стратегии первого игрока\n"
        for index in range(0, first_length):
            output += '{0}:{1} '.format(index, round(self.first[index], 2))
        output += " Всего: [{0}]\nСтратегии второго игрока\n".format(first_length)
        for index in range(0, second_length):
            output += "{0}:{1} ".format(index, round(self.second[index], 2))
        output += " Всего: [{0}]\n".format(second_length) + "Цена игры: {0}".format(round(self.game_price, 3))
        return output

    def __eq__(self, other):
        return self.game_price == other.game_price and self.first == other.first and self.second == other.second
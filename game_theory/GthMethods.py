__author__ = 'dimv36'
#coding: utf8
import random
from numpy import *
from entity import *


class GthMethods:
    @staticmethod
    def calc_alpha_beta(game_matrix):
        alpha_beta = AlphaBeta()
        alpha_beta.alpha = max(game_matrix.min(axis=1))
        alpha_beta.beta = min(game_matrix.max(axis=0))
        return alpha_beta

    @staticmethod
    def is_sp(alpha_beta):
        if abs(alpha_beta.alpha - alpha_beta.beta) < pow(10, -6):
            return True
        else:
            return False

    @staticmethod
    def calc_srp(game_matrix, error_value):
        iteration = 1
        strategy_first = random.randint(0, game_matrix.shape[0])
        strategy_array_first = game_matrix[strategy_first].copy()
        strategy_count_first = zeros(game_matrix.shape[0])
        strategy_count_second = zeros(game_matrix.shape[1])
        strategy_second = argmin(game_matrix[strategy_first])
        strategy_count_first[strategy_first] = 1
        strategy_count_second[strategy_second] = 1
        strategy_array_second = game_matrix[:, strategy_second].copy()
        while True:
            v_bot = min(strategy_array_first) / iteration
            v_top = max(strategy_array_second) / iteration
            strategy_first = argmax(strategy_array_second)
            strategy_array_first += game_matrix[strategy_first]
            strategy_second = argmin(strategy_array_first)
            strategy_array_second += game_matrix[:, strategy_second]
            strategy_count_first[strategy_first] += 1
            strategy_count_second[strategy_second] += 1
            iteration += 1
            if abs(v_bot - v_top) < error_value:
                price = abs((v_bot + v_top) / 2)
                distribution = SrpGamersProbabilityDistribution(strategy_count_first / iteration,
                                                                strategy_count_second / iteration,
                                                                price)
                return distribution

    @staticmethod
    def reduce(bi_matrix):

        def reduce_rows(bi_matrix):
            row_count = bi_matrix.row_count()
            for i in range(0, row_count):
                first_row = bi_matrix.first[i]
                for j in range(0, row_count):
                    if all(first_row >= bi_matrix.first[j]) and i != j:
                        bi_matrix.first = delete(bi_matrix.first, j, axis=0)
                        bi_matrix.second = delete(bi_matrix.second, j, axis=0)
                        return True
            return False

        def reduce_columns(bi_matrix):
            column_count = bi_matrix.column_count()
            for i in range(0, column_count):
                second_column = bi_matrix.second[:, i]
                for j in range(0, column_count):
                    if all(second_column >= bi_matrix.second[:, j]) and i != j:
                        bi_matrix.first = delete(bi_matrix.first, j, axis=1)
                        bi_matrix.second = delete(bi_matrix.second, j, axis=1)
                        return True
            return False

        while True:
            if False == reduce_rows(bi_matrix) and False == reduce_columns(bi_matrix):
                return bi_matrix

    @staticmethod
    def get_dominant_strategy(bi_matrix):
        bi_matrix_copy = BiMatrix.copy(bi_matrix)
        GthMethods.reduce(bi_matrix_copy)
        strategy = []
        for i in range(0, bi_matrix_copy.row_count()):
            for j in range(0, bi_matrix_copy.column_count()):
                bi_element = bi_matrix_copy.item(i, j)
                print(bi_element)
                strategy.append(bi_matrix.find(bi_element))
        strategy_first = GameStrategy(1, [])
        strategy_second = GameStrategy(2, [])
        for index in range(0, len(strategy)):
            strategy_first.add_strategy(strategy[index][0])
            strategy_second.add_strategy(strategy[index][1])
        return [strategy_first, strategy_second]

    @staticmethod
    def get_pareto_set(bi_matrix):
        result = []
        for i in range(0, bi_matrix.row_count()):
            for j in range(0, bi_matrix.column_count()):
                item = bi_matrix.item(i, j)
                other = bi_matrix.all_elements_without_current(i, j)
                is_in_pareto_set = True
                for element in other:
                    if not (item.first >= element.first or item.second >= element.second):
                        is_in_pareto_set = False
                if True == is_in_pareto_set:
                    result.append(item)
        return result

    @staticmethod
    def get_pareto_strategy(bi_matrix):
        strategy = []
        pareto_set = GthMethods.get_pareto_set(bi_matrix)
        for element in pareto_set:
            strategy.append(bi_matrix.find(element))
        strategy_first = GameStrategy(1, [])
        strategy_second = GameStrategy(2, [])
        for index in range(0, len(strategy)):
            strategy_first.add_strategy(strategy[index][0])
            strategy_second.add_strategy(strategy[index][1])
        return [strategy_first, strategy_second]

    @staticmethod
    def get_nash_equilibrium(bi_matrix):
        result = []
        for i in range(0, bi_matrix.row_count()):
            for j in range(0, bi_matrix.column_count()):
                item = bi_matrix.item(i, j)
                row_neighboring = bi_matrix.row_neighboring(i, j)
                column_neighboring = bi_matrix.column_neighboring(i, j)
                is_nash_on_row = True
                for element in row_neighboring:
                    if item.first < element.first:
                        is_nash_on_row = False
                is_nash_on_column = True
                for element in column_neighboring:
                    if item.second < element.second:
                        is_nash_on_column = False
                if True == is_nash_on_row and True == is_nash_on_column:
                    if not item in result:
                        result.append(item)
        return result

    @staticmethod
    def get_nash_equilibrium_mixed_strategy_2x2(bi_matrix):
        bi_matrix_copy = BiMatrix.copy(bi_matrix)
        f_matrix = array(bi_matrix_copy.first)
        s_matrix = array(bi_matrix_copy.second)
        f_prob = round((s_matrix[0, 0] - s_matrix[0, 1]) /
                            (s_matrix[0, 0] - s_matrix[1, 0] - s_matrix[0, 1] + s_matrix[1, 1]), 3)
        s_prob = round((f_matrix[0, 0] - f_matrix[1, 0]) /
                             (f_matrix[0, 0] - f_matrix[0, 1] - f_matrix[1, 0] + f_matrix[1, 1]), 3)
        print(f_prob, s_prob)
#        first = array([[f_prob, f_prob], [1 - f_prob, 1 - f_prob]])
#        second = array([[s_prob, 1 - s_prob], [s_prob, 1 - s_prob]])
#        prob_bi_matrix = BiMatrix(first, second)
#        print(prob_bi_matrix)
#        mixed_bi_matrix = bi_matrix_copy * prob_bi_matrix
#        return GthMethods.get_nash_equilibrium(mixed_bi_matrix)

if __name__ == "__main__":
#    bi_matrix = BiMatrix([[5, 9], [1, 2]], [[5, 1], [9, 2]])
#    bi_matrix = BiMatrix([[4, 0], [0, 1]], [[1, 0], [0, 4]])
    bi_matrix = BiMatrix([[6, 0], [0, 1]], [[1, 0], [0, 6]])
#    bi_matrix = BiMatrix([[5, 1], [3, 4]], [[5, 2], [1, 4]])
#    bi_matrix = BiMatrix([[3, -1], [-1, 0]], [[2, 3], [1, 0]])
#    print(GthMethods.get_nash_equilibrium(bi_matrix))
#    bi_matrix = BiMatrix([[-1, -5], [0, -3]], [[-1, 0], [-5, -3]])
    print(bi_matrix)
#    print(GthMethods.get_nash_equilibrium(bi_matrix))
    print(GthMethods.get_nash_equilibrium_mixed_strategy_2x2(bi_matrix))
#    print(GthMethods.get_nash_equilibrium_mixed_strategy_2x2(bi_matrix))
#    print(GthMethods.reduce(bi_matrix))

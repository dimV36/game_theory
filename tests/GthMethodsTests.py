__author__ = 'dimv36'

import unittest
from numpy import array
from GthMethods import GthMethods
from entity import *


class TestGthMethods(unittest.TestCase):
    def setUp(self):
        self.object = GthMethods()

    @staticmethod
    def print_srp(test_matrix):
        print("Matrix:")
        print(test_matrix)
        print(GthMethods.calc_srp(test_matrix, pow(10, -5)))
        print("\n")

    def test_calc_alpha_beta_1(self):
        game_matrix = array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
        alpha_beta = AlphaBeta(7., 7.)
        result = self.object.calc_alpha_beta(game_matrix)
        self.assertEqual(alpha_beta, result)

    def test_calc_alpha_beta_2(self):
        game_matrix = array([[2., 4., 1., 5.], [1., -1., 3., 2.], [5., 2., -4., 0.], [-2., 5., -3., -4.]])
        alpha_beta = AlphaBeta(1., 3.)
        result = self.object.calc_alpha_beta(game_matrix)
        self.assertEqual(alpha_beta, result)

    def test_calc_alpha_beta_3(self):
        game_matrix = array([[6., 2., 8., 7.], [9., 4., 8., 5.], [5., 3., 7., 4.]])
        alpha_beta = AlphaBeta(4., 4.)
        result = self.object.calc_alpha_beta(game_matrix)
        self.assertEqual(alpha_beta, result)

    def test_is_sp_1(self):
        alpha_beta = AlphaBeta(4., 4.)
        result = self.object.is_sp(alpha_beta)
        self.assertEqual(result, True)

    def test_is_sp_2(self):
        alpha_beta = AlphaBeta(4., 5.)
        result = self.object.is_sp(alpha_beta)
        self.assertEqual(result, False)

    @staticmethod
    def test_calc_srp_1():
        test_matrix = array([[7, 2, 9], [2, 9, 0], [9, 0, 11]])
        TestGthMethods.print_srp(test_matrix)
        pass

    @staticmethod
    def test_calc_srp_2():
        test_matrix = array([[-1, 0], [0, 1]])
        TestGthMethods.print_srp(test_matrix)
        pass

    @staticmethod
    def test_calc_srp_3():
        test_matrix = array([[0.32, 0], [0, 0.128]])
        TestGthMethods.print_srp(test_matrix)
        pass

    @staticmethod
    def test_calc_srp_4():
        test_matrix = array([[0.2, 0.4, 0.6, 0.4, 0.7], [0.3, 0.4, 0.6, 0.5, 0.8], [0.4, 0.5, 0.6, 0.5, 0.8],
                             [0.7, 0.3, 0.5, 0.2, 0.1]])
        TestGthMethods.print_srp(test_matrix)
        pass

    #Тесты для task03
    def test_reduce_1(self):
        bi_matrix = BiMatrix([[7, 5, 9], [6, 1, 0]], [[9, 4, 5], [8, 4, 1]])
        print(bi_matrix)
        result = BiMatrix([[7]], [[9]])
        calc_result = self.object.reduce(bi_matrix)
        print(calc_result)
        self.assertEqual(calc_result, result)

    def test_reduce_2(self):
        bi_matrix = BiMatrix([[7, 5, 10]], [[9, 4, 10]])
        print(bi_matrix)
        result = BiMatrix([[10]], [[10]])
        calc_result = self.object.reduce(bi_matrix)
        print(calc_result)
        self.assertEqual(calc_result, result)

    def test_get_dominant_strategy_1(self):
        bi_matrix = BiMatrix([[7, 5, 9], [6, 1, 0]], [[9, 4, 5], [8, 4, 1]])
        print(bi_matrix)
        calc_result = self.object.get_dominant_strategy(bi_matrix)
        strategy_1 = GameStrategy(1, [0])
        strategy_2 = GameStrategy(2, [0])
        print(calc_result)
        self.assertEqual(calc_result, [strategy_1, strategy_2])

    def test_get_dominant_strategy_2(self):
        bi_matrix = BiMatrix([[7, 5, 10]], [[9, 4, 10]])
        print(bi_matrix)
        calc_result = self.object.get_dominant_strategy(bi_matrix)
        strategy_1 = GameStrategy(1, [0])
        strategy_2 = GameStrategy(2, [2])
        print(calc_result)
        self.assertEqual(calc_result, [strategy_1, strategy_2])

    def test_get_pareto_set_1(self):
        bi_matrix = BiMatrix([[5, 1], [3, 4]], [[5, 2], [1, 4]])
        print(bi_matrix)
        result = [BiMatrix([[5]], [[5]])]
        calc_result = self.object.get_pareto_set(bi_matrix)
        print(calc_result)
        self.assertEqual(calc_result, result)

    def test_get_pareto_set_2(self):
        bi_matrix = BiMatrix([[4, 0], [0, 1]], [[1, 0], [0, 4]])
        print(bi_matrix)
        result = [BiMatrix([[4]], [[1]]), BiMatrix([[1]], [[4]])]
        calc_result = self.object.get_pareto_set(bi_matrix)
        print(calc_result)
        self.assertEqual(calc_result, result)

    def test_get_pareto_set_3(self):
        bi_matrix = BiMatrix([[5, 9], [1, 2]], [[5, 1], [9, 2]])
        print(bi_matrix)
        result = [BiMatrix([[5]], [[5]]), BiMatrix([[9]], [[1]]), BiMatrix([[1]], [[9]])]
        calc_result = self.object.get_pareto_set(bi_matrix)
        print(calc_result)
        self.assertEqual(calc_result, result)

    def test_get_pareto_strategy_1(self):
        bi_matrix = BiMatrix([[5, 1], [3, 4]], [[5, 2], [1, 4]])
        print(bi_matrix)
        calc_result = self.object.get_pareto_strategy(bi_matrix)
        strategy_1 = GameStrategy(1, [0])
        strategy_2 = GameStrategy(2, [0])
        print(calc_result)
        self.assertEqual(calc_result, [strategy_1, strategy_2])

    def test_get_pareto_strategy_2(self):
        bi_matrix = BiMatrix([[4, 0], [0, 1]], [[1, 0], [0, 4]])
        print(bi_matrix)
        calc_result = self.object.get_pareto_strategy(bi_matrix)
        strategy_1 = GameStrategy(1, [0, 1])
        strategy_2 = GameStrategy(2, [0, 1])
        print(calc_result)
        self.assertEqual(calc_result, [strategy_1, strategy_2])

    def test_get_pareto_strategy_3(self):
        bi_matrix = BiMatrix([[5, 9], [1, 2]], [[5, 1], [9, 2]])
        print(bi_matrix)
        calc_result = self.object.get_pareto_strategy(bi_matrix)
        strategy_1 = GameStrategy(1, [0, 1])
        strategy_2 = GameStrategy(2, [0, 1])
        print(calc_result)
        self.assertEqual(calc_result, [strategy_1, strategy_2])

    def test_get_nash_equilibrium_1(self):
        bi_matrix = BiMatrix([[5, 1], [3, 4]], [[5, 2], [1, 4]])
        print(bi_matrix)
        result = [BiMatrix([[5]], [[5]]), BiMatrix([[4]], [[4]])]
        calc_result = self.object.get_nash_equilibrium(bi_matrix)
        print(calc_result)
        self.assertEqual(calc_result, result)

    def test_get_nash_equilibrium_2(self):
        bi_matrix = BiMatrix([[4, 0], [0, 1]], [[1, 0], [0, 4]])
        print(bi_matrix)
        result = [BiMatrix([[4]], [[1]]), BiMatrix([[1]], [[4]])]
        calc_result = self.object.get_nash_equilibrium(bi_matrix)
        print(calc_result)
        self.assertEqual(calc_result, result)

    def test_get_nash_equilibrium_3(self):
        bi_matrix = BiMatrix([[5, 9], [1, 2]], [[5, 1], [9, 2]])
        print(bi_matrix)
        result = [BiMatrix([[5]], [[5]])]
        calc_result = self.object.get_nash_equilibrium(bi_matrix)
        print(calc_result)
        self.assertEqual(calc_result, result)

    def test_get_nash_equilibrium_mixed_strategy_2x2_1(self):
        bi_matrix = BiMatrix([[5, 1], [3, 4]], [[5, 2], [1, 4]])
        print(bi_matrix)
        result = [BiMatrix([[3.4]], [[3.0]])]
        calc_result = self.object.get_nash_equilibrium_mixed_strategy_2x2(bi_matrix)
        print(calc_result)
        self.assertEqual(calc_result, result)

    def test_get_nash_equilibrium_mixed_strategy_2x2_2(self):
        bi_matrix = BiMatrix([[4, 0], [0, 1]], [[1, 0], [0, 4]])
        print(bi_matrix)
        result = [BiMatrix([[0.8]], [[0.8]])]
        calc_result = self.object.get_nash_equilibrium_mixed_strategy_2x2(bi_matrix)
        print(calc_result)
        self.assertEqual(calc_result, result)

    def test_get_nash_equilibrium_mixed_strategy_2x2_3(self):
        bi_matrix = BiMatrix([[-10, 2], [1, -1]], [[5, -2], [-1, 1]])
        print(bi_matrix)
        result = [BiMatrix([[-0.571]], [[0.334]])]
        calc_result = self.object.get_nash_equilibrium_mixed_strategy_2x2(bi_matrix)
        print(calc_result)
        self.assertEqual(calc_result, result)

if __name__ == "__main__":
    unittest.main()

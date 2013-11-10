__author__ = 'dimv36'


class AlphaBeta:
    def __init__(self, alpha=0, beta=0):
        self.alpha = alpha
        self.beta = beta

    def __str__(self):
        return "alpha: {0}, beta: {1} ".format(self.alpha, self.beta)

    def __eq__(self, other):
        return self.alpha == other.alpha and self.beta == other.beta
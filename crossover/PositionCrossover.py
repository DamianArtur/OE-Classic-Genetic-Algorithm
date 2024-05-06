from random import random
from crossover.Crossover import Crossover

class PositionCrossover(Crossover):

    def __init__(self, population, probability, alpha=0.01, beta=0.02):
        super().__init__(population, probability)
        self._alpha = alpha
        self._beta = beta

    def crossover(self):
        population_size = len(self.population)

        for i in range(0, population_size - 1, 2):
            num_variables = len(self.population[0])
            for j in range(num_variables):
                if random() > 0.5:
                    self.population[i][j].value -= self._alpha
                    self.population[i + 1][j].value += self._beta
                else:
                    self.population[i][j].value += self._alpha
                    self.population[i + 1][j].value -= self._beta
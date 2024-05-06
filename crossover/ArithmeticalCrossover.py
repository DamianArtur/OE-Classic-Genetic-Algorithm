import numpy as np
from crossover.Crossover import Crossover

class ArithmeticalCrossover(Crossover):

    def crossover(self):
        population_size = len(self.population)
        for i in range(0, population_size - 1, 2):
            num_variables = len(self.population[0])
            alphas = np.random.uniform(0, 1, num_variables)

            if num_variables == 2:
                alphas[1] = 1 - alphas[0]
            for j in range(num_variables):
                value_1 = self.population[i][j].get_real_value()
                value_2 = self.population[i + 1][j].get_real_value()
                self.population[i][j].value += alphas[j] * (value_2 - value_1)
                self.population[i + 1][j].value += alphas[j] * (value_1 - value_2)
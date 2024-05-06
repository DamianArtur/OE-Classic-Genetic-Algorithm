import random
from crossover.Crossover import Crossover
class BLXAlphaBetaCrossover(Crossover):
    def crossover(self):
        population_size = len(self.population)
        for i in range(0, population_size - 1, 2):
            num_variables = len(self.population[0])
            offspring_1 = []
            offspring_2 = []

            for j in range(num_variables):
                parent_1_value = self.population[i][j].get_real_value()
                parent_2_value = self.population[i + 1][j].get_real_value()

                dx = abs(parent_1_value - parent_2_value)
                min_val = min(parent_1_value, parent_2_value)
                max_val = max(parent_1_value, parent_2_value)

                alpha = random.uniform(0,1)
                beta = random.uniform(0,1)

                min_range_offspring_1 = min_val - alpha * dx
                max_range_offspring_1 = max_val + beta * dx
                offspring_1_value = random.uniform(min_range_offspring_1, max_range_offspring_1)

                min_range_offspring_2 = min_val - alpha * dx
                max_range_offspring_2 = max_val + beta * dx
                offspring_2_value = random.uniform(min_range_offspring_2, max_range_offspring_2)

                offspring_1.append(offspring_1_value)
                offspring_2.append(offspring_2_value)

            for j in range(num_variables):
                self.population[i][j].value = offspring_1[j]
                self.population[i + 1][j].value = offspring_2[j]
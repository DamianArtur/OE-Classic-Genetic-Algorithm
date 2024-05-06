import random
from crossover.Crossover import Crossover

class MultipleCrossover(Crossover):
    def crossover(self):
        population_size = len(self.population)
        num_variables = len(self.population[0])
        children = []
        for j in range(population_size):
            child = []
            for i in range(num_variables):
                alpha = random.randint(0, population_size - 1)
                child.append(self.population[alpha][i].get_real_value())
            children.append(child)

        for i in range(population_size):
            for j in range(num_variables):
                self.population[i][j].value = children[i][j]
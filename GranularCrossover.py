import random

from Crossover import Crossover

class GranularCrossover(Crossover):

    def crossover(self):
        for i in range(0, len(self.population), 2):
            if random.random() < self.probability:
                for j in range(self.population[i].total_length):
                    if random.random() < 0.5:
                        self.population[i].bits[j], self.population[i+1].bits[j] \
                            = self.population[i].bits[j], self.population[i].bits[j]
                    else:
                        self.population[i].bits[j], self.population[i+1].bits[j] \
                            = self.population[i + 1].bits[j], self.population[i + 1].bits[j]
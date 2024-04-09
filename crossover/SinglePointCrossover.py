import random

from crossover.Crossover import Crossover

class SinglePointCrossover(Crossover):

    def crossover(self):
        for i in range(0, len(self.population), 2):
            if random.random() < self.probability:
                crossover_point = random.randint(1, self.population[i].total_length - 1)

                self.population[i].bits, self.population[i+1].bits \
                    = self.population[i].bits[:crossover_point] + self.population[i+1].bits[crossover_point:], \
                      self.population[i+1].bits[:crossover_point] + self.population[i].bits[crossover_point:]
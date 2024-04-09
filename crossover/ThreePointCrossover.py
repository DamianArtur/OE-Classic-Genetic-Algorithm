import random

from crossover.Crossover import Crossover

class ThreePointCrossover(Crossover):

    def crossover(self):
        for i in range(0, len(self.population), 2):
            if random.random() < self.probability:

                crossover_point1 = random.randint(1, self.population[i].total_length - 3)
                crossover_point2 = random.randint(crossover_point1 + 1, self.population[i].total_length - 2)
                crossover_point3 = random.randint(crossover_point2 + 1, self.population[i].total_length - 1)

                self.population[i].bits, self.population[i+1].bits \
                    = self.population[i].bits[:crossover_point1] + self.population[i+1].bits[crossover_point1:crossover_point2] + self.population[i].bits[crossover_point2:crossover_point3] + self.population[i+1].bits[crossover_point3:], \
                      self.population[i+1].bits[:crossover_point1] + self.population[i].bits[crossover_point1:crossover_point2] + self.population[i+1].bits[crossover_point2:crossover_point3] + self.population[i].bits[crossover_point3:]
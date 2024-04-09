import random

from crossover.Crossover import Crossover

class SinglePointCrossover(Crossover):

    def crossover(self):
        population_size = len(self.population)
        for i in range(0, population_size - 1, 2):
            if random.random() < self.probability:
                crossover_point = random.randint(1, self.population[i].total_length - 1)

                self.population[i].bits, self.population[i + 1].bits \
                    = self.population[i].bits[:crossover_point] + self.population[i + 1].bits[crossover_point:], \
                      self.population[i + 1].bits[:crossover_point] + self.population[i].bits[crossover_point:]


        if population_size % 2 == 1:
            last_individual_index = population_size - 1
            if random.random() < self.probability:
                crossover_point = random.randint(1, self.population[last_individual_index].total_length - 1)

                self.population[last_individual_index].bits \
                    = self.population[last_individual_index].bits[:crossover_point] + \
                      self.population[last_individual_index].bits[crossover_point:]

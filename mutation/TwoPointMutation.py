import random

from mutation.Mutation import Mutation

class TwoPointMutation(Mutation):

    def mutate(self):
        for individual in self.population:
            if random.random() < self.probability:
                mutation_point1 = random.randint(0, len(individual.bits) - 1)
                mutation_point2 = random.randint(0, len(individual.bits) - 1)
                individual.bits[mutation_point1], individual.bits[mutation_point2] = individual.bits[mutation_point2], individual.bits[mutation_point1]
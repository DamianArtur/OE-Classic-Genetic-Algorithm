import random

from mutation.Mutation import Mutation

class SinglePointMutation(Mutation):

    def mutate(self):
        for individual in self.population:
            if random.random() < self.probability:
                mutation_point = random.randint(0, len(individual) - 1)
                individual.bits[mutation_point] = 1 - individual.bits[mutation_point]
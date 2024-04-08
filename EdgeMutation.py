import random

from Mutation import Mutation

class EdgeMutation(Mutation):

    def mutate(self):
        for individual in self.population:
            if random.random() < self.probability:
                individual.bits[-1] = 1 - individual.bits[-1]
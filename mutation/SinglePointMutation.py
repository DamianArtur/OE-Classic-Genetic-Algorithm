import random

from mutation.Mutation import Mutation

class SinglePointMutation(Mutation):

    def mutate(self):
        for individual in self.population:
            if random.random() < self.probability:
                for i in individual:
                    mutation_point = random.randint(0, len(i.bits) - 1)
                    i.bits[mutation_point] = 1 - i.bits[mutation_point]
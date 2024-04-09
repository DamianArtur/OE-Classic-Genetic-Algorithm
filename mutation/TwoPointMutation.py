import random

from mutation.Mutation import Mutation

class TwoPointMutation(Mutation):

    def mutate(self):
        for individual in self.population:
            if random.random() < self.probability:
                for i in individual:
                    mutation_point1 = random.randint(0, len(i.bits) - 1)
                    mutation_point2 = random.randint(0, len(i.bits) - 1)
                    i.bits[mutation_point1], i.bits[mutation_point2] = i.bits[mutation_point2], i.bits[mutation_point1]
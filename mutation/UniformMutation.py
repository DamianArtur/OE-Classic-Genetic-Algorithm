import random

from mutation.Mutation import Mutation
class UniformMutation(Mutation):
    def mutate(self):
        for individual in self.population:
            for i in range(len(individual)):
                if random.random() < self.probability:
                    individual[i] = random.uniform(min(individual), max(individual))

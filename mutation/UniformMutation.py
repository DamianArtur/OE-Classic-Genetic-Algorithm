import random

from mutation.Mutation import Mutation

class UniformMutation(Mutation):
    def mutate(self):
        for individual in self.population:
            for i in range(len(individual)):
                if random.random() < self.probability:
                    individual[i] = random.uniform(min(individual), max(individual))

# Przykład użycia
if __name__ == "__main__":
    # Populacja
    population = [[2, 3]]

    # Prawdopodobieństwo mutacji
    probability = 0.5

    mutation_operator = UniformMutation(population, probability)

    print("Before Mutation:", population)

    mutation_operator.mutate()

    print("After Mutation:", population)
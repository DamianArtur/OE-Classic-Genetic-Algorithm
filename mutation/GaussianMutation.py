import numpy as np

class GaussianMutation:
    def __init__(self, population, sigma):
        self.population = population
        self.sigma = sigma

    def mutate(self):
        mutated_population = []
        for individual in self.population:
            mutated_individual = []
            for gene in individual:
                mutated_gene = gene + np.random.normal(0, self.sigma)
                mutated_individual.append(mutated_gene)
            mutated_population.append(mutated_individual)
        return mutated_population

# Przykład użycia
if __name__ == "__main__":
    # Populacja
    population = [[2, 3]]

    # Odchylenie standardowe mutacji
    sigma = 1

    mutation_operator = GaussianMutation(population, sigma)

    print("Before Mutation:", population)

    mutated_population = mutation_operator.mutate()

    print("After Mutation:", mutated_population)

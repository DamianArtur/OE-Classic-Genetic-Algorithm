from crossover.Crossover import Crossover
class AverageCrossover(Crossover):
    def crossover(self):
        population_size = len(self.population)
        for i in range(0, population_size - 1, 2):
            num_variables = len(self.population[0])
            offspring_1 = []
            offspring_2 = []

            for j in range(num_variables):
                parent_1_value = self.population[i][j].get_real_value()
                parent_2_value = self.population[i + 1][j].get_real_value()

                offspring_1_value = (parent_1_value + parent_2_value) / 2
                offspring_2_value = (parent_1_value + parent_2_value) / 2

                offspring_1.append(offspring_1_value)
                offspring_2.append(offspring_2_value)
                self.population[i][j].value = offspring_1[j]
                self.population[i + 1][j].value = offspring_2[j]

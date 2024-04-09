class EliteSelection:
    def __init__(self, population, elite_strategy_amount, function,maximization):
        self.population = population
        self.elite_strategy_amount = elite_strategy_amount
        self.function = function
        self.maximization = maximization
    def select_elites(self):
        if self.maximization:
            sorted_population = sorted(self.population.get_population(),
                                       key=lambda x: self.function.compute(x.get_real_value()),reverse=True)
        else:
            sorted_population = sorted(self.population.get_population(),
                                       key=lambda x: self.function.compute(x.get_real_value()))

        elites = sorted_population[:self.elite_strategy_amount]

        return elites
    def get_population_value(self):
        return [chromosome.get_real_value() for chromosome in self.population]
    def apply_elites(self, elites):
        self.population.population.sort(key=lambda x: x.fitness)
        self.population.population[:self.elite_strategy_amount] = elites
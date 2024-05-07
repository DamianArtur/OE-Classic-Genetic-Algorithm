class EliteSelection:
    def __init__(self, population, elite_amount, function, maximization):
        self.population = population
        self.elite_amount = elite_amount
        self.function = function
        self.maximization = maximization

    def select_elites(self):
        sorted_population = sorted(self.population.get_population(), key=lambda x: self.function.compute([chromosome.get_real_value() for chromosome in x]))
        if self.maximization:
            return sorted_population[-self.elite_amount:]
        else:
            return sorted_population[:self.elite_amount]

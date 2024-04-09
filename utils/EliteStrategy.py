class EliteSelection:
    def __init__(self, population, elite_strategy_amount):
        self.population = population
        self.elite_strategy_amount = elite_strategy_amount

    def select_elites(self):
        elites = sorted(self.population.population, key=lambda x: x.get_real_value())[:self.elite_strategy_amount]
        return elites

    def apply_elites(self, elites):
        self.population.population.sort(key=lambda x: x.fitness)
        self.population.population[:self.elite_strategy_amount] = elites
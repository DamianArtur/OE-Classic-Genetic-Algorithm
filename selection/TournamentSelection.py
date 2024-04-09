import random

from selection.Selection import Selection

class TournamentSelection(Selection):

    def __init__(self, population, tournament_size):
        super().__init__(population)
        self.tournament_size = tournament_size

    def select(self):
        selected_individuals = []

        for _ in range(len(self.population.get_population())):
            tournament = random.sample(self.population.get_population_values(), self.tournament_size)
            
            if self.minimization:
                best_individual = min(tournament)
            else:
                best_individual = max(tournament)
                
            selected_individuals.append(best_individual)

        return selected_individuals

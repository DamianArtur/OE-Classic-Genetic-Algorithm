import os

import numpy as np
from matplotlib import pyplot as plt

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from selection.BestSelection import BestSelection
from mutation.EdgeMutation import EdgeMutation
from crossover.GranularCrossover import GranularCrossover
from utils.EliteStrategy import EliteSelection
from utils.Inversion import InversionOperator
from utils.Population import Population
from selection.RouletteWheelSelection import RouletteWheelSelection
from crossover.SinglePointCrossover import SinglePointCrossover
from mutation.SinglePointMutation import SinglePointMutation
from crossover.ThreePointCrossover import ThreePointCrossover
from selection.TournamentSelection import TournamentSelection
from crossover.TwoPointCrossover import TwoPointCrossover
from mutation.TwoPointMutation import TwoPointMutation
from crossover.UniformCrossover import UniformCrossover

from functions.StyblinskiTang import StyblinskiTang
from functions.Rosenbrock import Rosenbrock

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Projekt 2")
        self.pack(padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):

        self.function_label = tk.Label(self, text="Choose funcion")
        self.function_label.pack()
        
        self.function_combo = ttk.Combobox(self, width=30)
        self.function_combo['values'] =['Styblinski and Tang', 'Rosenbrock’s Function']
        self.function_combo.set('Styblinski and Tang')
        self.function_combo.pack(pady=5)

        self.input_fields = ["begin of the range", "end of the range", "population amount", "number of bits", "epochs amount",
                             "best and tournament chromosome amount", "elite strategy amount",
                             "cross probability", "mutation probability", "inversion probability"]
        self.entries = {}
        self.example_values = ["-10", "10", "100", "20", "100", "20", "5", "0.7", "0.01", "0.01"]
        for field, example_value in zip(self.input_fields, self.example_values):
            label = tk.Label(self, text=field)
            label.pack()
            self.entries[field] = tk.Entry(self)
            self.entries[field].insert(0, example_value)
            self.entries[field].pack(pady=5)


        self.selection_method_label = tk.Label(self, text="Choose selection method")
        self.selection_method_label.pack()

        self.selection_method_combo = ttk.Combobox(self, width=30)
        self.selection_method_combo['values'] = ['BEST', 'ROULETTE', 'TOURNAMENT']
        self.selection_method_combo.set('BEST')
        self.selection_method_combo.pack(pady=5)


        self.crossover_method_label = tk.Label(self, text="Choose crossover method")
        self.crossover_method_label.pack()


        self.crossover_method_combo = ttk.Combobox(self, width=30)
        self.crossover_method_combo['values'] = ['ONE_POINT', 'TWO_POINT', 'UNIFORM', 'THREE_POINT', 'GRANULAR']
        self.crossover_method_combo.set('ONE_POINT')
        self.crossover_method_combo.pack(pady=5)

        self.mutation_method_label = tk.Label(self, text="Choose mutation method")
        self.mutation_method_label.pack()

        self.mutation_method_combo = ttk.Combobox(self, width=30)
        self.mutation_method_combo['values'] = ['EDGE_MUTATION', 'TWO_POINT_MUTATION', 'SINGLE_POINT_MUTATION']
        self.mutation_method_combo.set('EDGE_MUTATION')
        self.mutation_method_combo.pack(pady=5)

        # self.max_min_combo = ttk.Combobox(self, width=30)
        # self.max_min_combo.pack(pady=5)
        self.maximization_var = tk.BooleanVar()
        self.max_min_checkbutton = tk.Checkbutton(self, text="Maximization", variable=self.maximization_var)
        self.max_min_checkbutton.pack(pady=5)

        self.execute_button = tk.Button(self, text="Execute",
                                      command=self.execute)
        self.execute_button.pack(pady=5)
        
    def execute(self):
        function = self.function_combo.get()
        if function == 'Styblinski and Tang':
            function = StyblinskiTang()
        elif function == 'Rosenbrock’s Function':
            function = Rosenbrock()

        a = float(
            self.entries["begin of the range"].get())
        b = float(
            self.entries["end of the range"].get())
        precision = int(
            self.entries["number of bits"].get())
        epochs = int(
            self.entries["epochs amount"].get())
        population_size = int(
            self.entries["population amount"].get())
        best_and_tournament = int(
            self.entries["best and tournament chromosome amount"].get())
        elite_strategy_amount = int(
            self.entries["elite strategy amount"].get())
        mutation_probability = float(
            self.entries["mutation probability"].get())
        crossover_probability = float(
            self.entries["cross probability"].get())
        inversion_probability = float(
            self.entries["inversion probability"].get())
        population = Population(population_size, a, b, precision)

        best_individual_x = None
        best_individual_y = float('inf')
        bests = []
        means = []
        stds = []
        for _ in range(epochs):
            non_elite_population = Population(population_size - elite_strategy_amount, a, b, precision)
            elite_strategy = EliteSelection(population, elite_strategy_amount, function)
            elites = elite_strategy.select_elites()
            population.population[:elite_strategy_amount] = elites
            population.population[elite_strategy_amount:] = non_elite_population.population
            selection_method = self.selection_method_combo.get()
            if selection_method == 'BEST':
                selection_strategy = BestSelection(population, function)
            elif selection_method == 'ROULETTE':
                selection_strategy = RouletteWheelSelection(population, function)
            elif selection_method == 'TOURNAMENT':
                selection_strategy = TournamentSelection(population, function, best_and_tournament)

            crossover_method = self.crossover_method_combo.get()
            crossover_operator = None
            if crossover_method == 'ONE_POINT':
                crossover_operator = SinglePointCrossover(population.get_population(), crossover_probability)
            elif crossover_method == 'TWO_POINT':
                crossover_operator = TwoPointCrossover(population.get_population(), crossover_probability)
            elif crossover_method == 'UNIFORM':
                crossover_operator = UniformCrossover(population.get_population(), crossover_probability)
            elif crossover_method == 'THREE_POINT':
                crossover_operator = ThreePointCrossover(population.get_population(), crossover_probability)
            elif crossover_method == 'GRANULAR':
                crossover_operator = GranularCrossover(population.get_population(), crossover_probability)

            mutation_method = self.mutation_method_combo.get()
            mutation_operator = None
            if mutation_method == 'EDGE_MUTATION':
                mutation_operator = EdgeMutation(population.get_population(), mutation_probability)
            elif mutation_method == 'TWO_POINT_MUTATION':
                mutation_operator = TwoPointMutation(population.get_population(), mutation_probability)
            elif mutation_method == 'SINGLE_POINT_MUTATION':
                mutation_operator = SinglePointMutation(population.get_population(), mutation_probability)

            inversion_operator = InversionOperator(inversion_probability)
            # print("Do inwersji:")
            # for i in range (0,4):
            #     print(population.population[i].bits)
            # for i in range (0,population_size):
            #     inversion_operator.apply(population.population[i].bits)
            # print("Po inwersji:")
            # for i in range (0,4):
            #     print(population.population[i].bits)


            values = [function.compute(individual) for individual in population.get_population_value()]
            print(np.min(values))
            current_best_y = np.min(values)

            if current_best_y < best_individual_y:
                best_individual_y = current_best_y
                best_individaul_index = values.index(current_best_y)
                best_individual_x = population.get_population_value()[best_individaul_index]

            bests.append(np.min(values))
            means.append(np.mean(values))
            stds.append(np.std(values))

            selection_strategy.select()
            crossover_operator.crossover()
            mutation_operator.mutate()






        if not os.path.exists('output'):
            os.makedirs('output')

        plt.plot(bests)
        plt.savefig('output/bests.png')
        plt.clf()

        plt.plot(means)
        plt.savefig('output/means.png')
        plt.clf()

        plt.plot(stds)
        plt.savefig('output/stds.png')
        plt.clf()

        plt.close('all')

        tk.messagebox.showinfo('Wynik', f'f({best_individual_x}) = {best_individual_y}')

    def clear_placeholder(self, event):
        event.widget.delete(0, "end")
import tkinter as tk
from tkinter import ttk

from BestSelection import BestSelection
from EdgeMutation import EdgeMutation
from GranularCrossover import GranularCrossover
from Inversion import InversionOperator
from Population import Population
from RouletteWheelSelection import RouletteWheelSelection
from SinglePointCrossover import SinglePointCrossover
from SinglePointMutation import SinglePointMutation
from ThreePointCrossover import ThreePointCrossover
from TournamentSelection import TournamentSelection
from TwoPointCrossover import TwoPointCrossover
from TwoPointMutation import TwoPointMutation
from UniformCrossover import UniformCrossover


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=10, pady=10)
        self.create_widgets()
    def create_widgets(self):

        self.function_label = tk.Label(self, text="Choose funcion")
        self.function_label.pack()
        
        self.function_combo = ttk.Combobox(self, width=30)
        self.function_combo['values'] =['Styblinski and Tang', 'Rosenbrock’s Function']
        self.function_combo.pack(pady=5)

        self.input_fields = ["begin of the range", "end of the range", "population amount", "number of bits", "epochs amount",
                             "best and tournament chromosome amount", "elite strategy amount",
                             "cross probability", "mutation probability", "inversion probability"]
        self.entries = {}
        for field in self.input_fields:
            self.entries[field] = tk.Entry(self)
            self.entries[field].insert(0, field)
            self.entries[field].bind("<FocusIn>", self.clear_placeholder)
            self.entries[field].pack(pady=5)


        self.selection_method_label = tk.Label(self, text="Choose selection method")
        self.selection_method_label.pack()

        self.selection_method_combo = ttk.Combobox(self, width=30)
        self.selection_method_combo['values'] = ['BEST', 'ROULETTE', 'TOURNAMENT']
        self.selection_method_combo.pack(pady=5)


        self.crossover_method_label = tk.Label(self, text="Choose crossover method")
        self.crossover_method_label.pack()


        self.crossover_method_combo = ttk.Combobox(self, width=30)
        self.crossover_method_combo['values'] = ['ONE_POINT', 'TWO_POINT', 'UNIFORM', 'THREE_POINT', 'GRANULAR']
        self.crossover_method_combo.pack(pady=5)

        self.mutation_method_label = tk.Label(self, text="Choose mutation method")
        self.mutation_method_label.pack()

        self.mutation_method_combo = ttk.Combobox(self, width=30)
        self.mutation_method_combo['values'] = ['EDGE_MUTATION', 'TWO_POINT_MUTATION', 'SINGLE_POINT_MUTATION']
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
        a = int(
            self.entries["begin of the range"].get())
        b = int(
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

        population = Population(population_size,a,b,precision)

        selection_method = self.selection_method_combo.get()
        if selection_method == 'BEST':
            selection_strategy = BestSelection(population)
        elif selection_method == 'ROULETTE':
            selection_strategy = RouletteWheelSelection(population)
        elif selection_method == 'TOURNAMENT':
            selection_strategy = TournamentSelection(population, best_and_tournament)

        selected_individuals = selection_strategy.select()
        crossover_method = self.crossover_method_combo.get()
        crossover_operator = None
        if crossover_method == 'ONE_POINT':
            crossover_operator = SinglePointCrossover(population, crossover_probability)
        elif crossover_method == 'TWO_POINT':
            crossover_operator = TwoPointCrossover(population, crossover_probability)
        elif crossover_method == 'UNIFORM':
            crossover_operator = UniformCrossover(population, crossover_probability)
        elif crossover_method == 'THREE_POINT':
            crossover_operator = ThreePointCrossover(population, crossover_probability)
        elif crossover_method == 'GRANULAR':
            crossover_operator = GranularCrossover(population, crossover_probability)

        if crossover_operator:
            crossover_operator.crossover()

        mutation_method = self.mutation_method_combo.get()
        mutation_operator = None
        if mutation_method == 'EDGE_MUTATION':
            mutation_operator = EdgeMutation(population, mutation_probability)
        elif mutation_method == 'TWO_POINT_MUTATION':
            mutation_operator = TwoPointMutation(population, mutation_probability)
        elif mutation_method == 'SINGLE_POINT_MUTATION':
            mutation_operator = SinglePointMutation(population, mutation_probability)

        if mutation_operator:
            mutation_operator.mutate()
        inversion_operator = InversionOperator(inversion_probability)
        print("Do inwersji:")
        for i in range (0,4):
            print(population.population[i].bits)
        for i in range (0,population_size):
            inversion_operator.apply(population.population[i].bits)
        print("Po inwersji:")
        for i in range (0,4):
            print(population.population[i].bits)


    def clear_placeholder(self, event):
        event.widget.delete(0, "end")
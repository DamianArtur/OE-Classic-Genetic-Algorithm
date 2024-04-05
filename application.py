import tkinter as tk
from tkinter import ttk

from BinaryChromosome import GeneticAlgorithm
from Inversion import InversionOperator


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        self.function_combo = ttk.Combobox(self, width=30)
        self.function_combo.pack(pady=5)

        self.input_fields = ["begin of the range", "end of the range", "population amount", "number of bits", 
                             "best and tournament chromosome amount", "elite strategy amount", 
                             "cross probability", "mutation probability", "inversion probability"]
        self.entries = {}
        for field in self.input_fields:
            self.entries[field] = tk.Entry(self)
            self.entries[field].insert(0, field)
            self.entries[field].bind("<FocusIn>", self.clear_placeholder)
            self.entries[field].pack(pady=5)

        self.selection_combo = ttk.Combobox(self, width=30)
        self.selection_combo.pack(pady=5)

        self.cross_combo = ttk.Combobox(self, width=30)
        self.cross_combo.pack(pady=5)

        self.mutation_combo = ttk.Combobox(self, width=30)
        self.mutation_combo.pack(pady=5)

        self.max_min_combo = ttk.Combobox(self, width=30)
        self.max_min_combo.pack(pady=5)
        self.apply_button = tk.Button(self, text="Apply Inversion Probability",
                                      command=self.apply_inversion_probability)
        self.apply_button.pack(pady=5)

    def apply_inversion_probability(self):
        inversion_probability = float(
            self.entries["inversion probability"].get())
        a = int(
            self.entries["begin of the range"].get())
        b = int(
            self.entries["end of the range"].get())
        precision = int(
            self.entries["number of bits"].get())
        population_size = int(
            self.entries["population amount"].get())
        geneticAlgorithm = GeneticAlgorithm(population_size,a,b,precision,100)
        inversion_operator = InversionOperator(inversion_probability)
        print("Do inwersji:")
        for i in range (0,4):
            print(geneticAlgorithm.population[i].bits)
        for i in range (0,population_size):
            inversion_operator.apply(geneticAlgorithm.population[i].bits)
        print("Po inwersji:")
        for i in range (0,4):
            print(geneticAlgorithm.population[i].bits)

    def clear_placeholder(self, event):
        event.widget.delete(0, "end")
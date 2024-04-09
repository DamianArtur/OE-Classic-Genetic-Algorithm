import random


class InversionOperator:
    def __init__(self, probability,BinaryChromosome):
        self.probability = probability
        self.chromosome = BinaryChromosome

    def apply(self):
        randomProb = random.random()

        if randomProb < self.probability:
            point1 = random.randint(0, len(self.chromosome.bits) - 1)
            point2 = random.randint(0, len(self.chromosome.bits) - 1)
            if point1 > point2:
                point1, point2 = point2, point1
            self.chromosome.bits[point1:point2 + 1] = reversed(self.chromosome.bits[point1:point2 + 1])
import random


class InversionOperator:
    def __init__(self, probability):
        self.probability = probability

    def apply(self, chromosome):
        randomProb = random.random()

        if randomProb < self.probability:
            point1 = random.randint(0, len(chromosome) - 1)
            point2 = random.randint(0, len(chromosome) - 1)
            if point1 > point2:
                point1, point2 = point2, point1
            chromosome[point1:point2 + 1] = reversed(chromosome[point1:point2 + 1])
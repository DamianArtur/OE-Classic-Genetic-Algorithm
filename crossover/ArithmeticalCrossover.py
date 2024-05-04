import random

class ArithmeticalCrossover:

    def crossover(self, parent_x, parent_y, alpha):
        assert len(parent_x) == len(parent_y)
        child_x = [alpha * parent_x[i] + (1 - alpha) * parent_y[i] for i in range(len(parent_x))]
        child_y = [alpha * parent_y[i] + (1 - alpha) * parent_x[i] for i in range(len(parent_y))]

        return child_x, child_y


parent_x = [2, 3]
parent_y = [4, 8]

print("Parent X:", parent_x)
print("Parent Y:", parent_y)

crossover_operator = ArithmeticalCrossover()

alpha = 0.25
print("Alpha:", alpha)

child_x, child_y = crossover_operator.crossover(parent_x, parent_y, alpha)

print("Child X:", child_x)
print("Child Y:", child_y)


class MultiArithmeticalCrossover:
    def crossover(self, parent_x, parent_y, parent_z, alphas):
        assert len(parent_x) == len(parent_y) == len(parent_z)

        child_1 = [alphas[0] * parent_x[i] + alphas[1] * parent_y[i] + alphas[2] * parent_z[i] for i in
                   range(len(parent_x))]
        child_2 = [alphas[0] * parent_x[i + 1] + alphas[1] * parent_y[i + 1] + alphas[2] * parent_z[i + 1] for i in
                   range(len(parent_x) - 1)]

        return child_1, child_2

if __name__ == "__main__":

    parent_x = [2, 3]
    parent_y = [4, 8]
    parent_z = [7, 9]

    print("Parent X:", parent_x)
    print("Parent Y:", parent_y)
    print("Parent Z:", parent_z)

    alphas = [0.2, 0.3, 0.5]
    print("Alphas:", alphas)

    multi_crossover_operator = MultiArithmeticalCrossover()

    child_1, child_2 = multi_crossover_operator.crossover(parent_x, parent_y, parent_z, alphas)
    print("Child 1:", child_1)
    print("Child 2:", child_2)
import random


class BLXAlphaBetaCrossover:
    def crossover(self, parent_1, parent_2, alpha, beta):
        assert len(parent_1) == len(parent_2) == 2

        dx = abs(parent_1[0] - parent_2[0])
        dy = abs(parent_1[1] - parent_2[1])

        print("dx:", dx)
        print("dy:", dy)

        child_1 = []
        child_2 = []

        # Obliczanie wspólnych wartości min i max dla obu potomków
        min_val_x = min(parent_1[0], parent_2[0])
        max_val_x = max(parent_1[0], parent_2[0])
        min_val_y = min(parent_1[1], parent_2[1])
        max_val_y = max(parent_1[1], parent_2[1])

        # Generowanie nowych wartości dla potomka 1
        min_range_child_x = min_val_x - alpha * dx
        max_range_child_x = max_val_x + beta * dx
        print("x1new = liczba wylosowana z [", min_range_child_x, ",", max_range_child_x, "]")
        child_1_x_gene = random.uniform(min_range_child_x, max_range_child_x)
        child_1.append(child_1_x_gene)

        min_range_child_y = min_val_y - alpha * dy
        max_range_child_y = max_val_y + beta * dy
        print("y1new = liczba wylosowana z [", min_range_child_y, ",", max_range_child_y, "]")
        child_1_y_gene = random.uniform(min_range_child_y, max_range_child_y)
        child_1.append(child_1_y_gene)

        # Generowanie nowych wartości dla potomka 2
        min_range_child_x = min_val_x - alpha * dx
        max_range_child_x = max_val_x + beta * dx
        print("x2new = liczba wylosowana z [", min_range_child_x, ",", max_range_child_x, "]")
        child_2_x_gene = random.uniform(min_range_child_x, max_range_child_x)
        child_2.append(child_2_x_gene)

        min_range_child_y = min_val_y - alpha * dy
        max_range_child_y = max_val_y + beta * dy
        print("y2new = liczba wylosowana z [", min_range_child_y, ",", max_range_child_y, "]")
        child_2_y_gene = random.uniform(min_range_child_y, max_range_child_y)
        child_2.append(child_2_y_gene)

        return child_1, child_2


# Przykład do testowania
if __name__ == "__main__":
    # Osobniki rodzicielskie
    parent_1 = [2, 3]
    parent_2 = [4, 8]

    print("Parent 1:", parent_1)
    print("Parent 2:", parent_2)

    # Parametry alpha i beta
    alpha = 0.25
    beta = 0.7
    print("Alpha:", alpha)
    print("Beta:", beta)

    # Tworzenie instancji klasy BLXAlphaBetaCrossover
    blx_crossover_operator = BLXAlphaBetaCrossover()

    # Krzyżowanie BLX-a-b
    child_1, child_2 = blx_crossover_operator.crossover(parent_1, parent_2, alpha, beta)

    print("Child 1:", child_1)
    print("Child 2:", child_2)

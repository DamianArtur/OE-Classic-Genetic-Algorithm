import random


class BlendCrossover:
    def crossover(self, parent_1, parent_2, alpha):
        assert len(parent_1) == len(parent_2) == 2
        d1 = abs(parent_1[0] - parent_2[0])
        d2 = abs(parent_1[1] - parent_2[1])

        print("d1:", d1)
        print("d2:", d2)

        child_1 = []
        child_2 = []

        min_val_x = min(parent_1[0], parent_2[0])
        max_val_x = max(parent_1[0], parent_2[0])
        min_val_y = min(parent_1[1], parent_2[1])
        max_val_y = max(parent_1[1], parent_2[1])

        for i in range(2):

            # Generowanie nowej wartości dla potomka 1
            min_range_child_1 = min_val_x - alpha * d1
            max_range_child_1 = max_val_x + alpha * d1
            print("[", min_range_child_1, ",", max_range_child_1, "]")
            child_1_gene = random.uniform(min_range_child_1, max_range_child_1)
            child_1.append(child_1_gene)

            # Generowanie nowej wartości dla potomka 2
            min_range_child_2 = min_val_y - alpha * d2
            max_range_child_2 = max_val_y + alpha * d2
            print("[", min_range_child_2, ",", max_range_child_2, "]")
            child_2_gene = random.uniform(min_range_child_2, max_range_child_2)
            child_2.append(child_2_gene)

        return child_1, child_2


# Przykład do testowania
if __name__ == "__main__":
    blend_crossover_operator = BlendCrossover()
    parent_1 = [2, 3]
    parent_2 = [4, 8]
    print("Parent 1:", parent_1)
    print("Parent 2:", parent_2)
    alpha = 0.25
    print("Alpha:", alpha)
    child_1, child_2 = blend_crossover_operator.crossover(parent_1, parent_2, alpha)
    print("Child 1:", child_1)
    print("Child 2:", child_2)

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

            min_range_child_1 = min_val_x - alpha * d1
            max_range_child_1 = max_val_x + alpha * d1
            print("[", min_range_child_1, ",", max_range_child_1, "]")
            child_1_gene = random.uniform(min_range_child_1, max_range_child_1)
            child_1.append(child_1_gene)

            min_range_child_2 = min_val_y - alpha * d2
            max_range_child_2 = max_val_y + alpha * d2
            print("[", min_range_child_2, ",", max_range_child_2, "]")
            child_2_gene = random.uniform(min_range_child_2, max_range_child_2)
            child_2.append(child_2_gene)

        return child_1, child_2
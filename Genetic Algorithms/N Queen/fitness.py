from constants import *


def get_cost(gens):
    cost = 0
    range_one = [i + 1 for i in range(len(gens))]
    range_two = [j + 1 for j in range(len(gens))]

    for rg_one in range_one:
        for rg_two in range_two:
            if rg_one != rg_two:
                rg_one_index = rg_one - 1
                rg_two_index = rg_two - 1
                if gens[rg_one_index] == gens[rg_two_index]:
                    cost += 1
                if abs(rg_one - rg_two) == abs(gens[rg_one_index] - gens[rg_two_index]):
                    cost += 1
    return cost


def fitness_chromosomes():
    for chromosome in chromosomes_list:
        if chromosome["cost"] == 0:
            cost = get_cost(chromosome["gens"])
            chromosome["cost"] = cost

import random as rd
from constants import *


def cost_of_imperialist():
    list_of_imperialist = [empire["imperialist"] for empire in empires]
    imperialist_cost = [imperialist["cost"] for imperialist in list_of_imperialist]
    return imperialist_cost


def take_half_randomly(chromosome):
    half_gens = QUEEN//2
    half = []
    half_index = []
    while len(half) < half_gens:
        random_index = rd.randint(0, QUEEN-1)
        random_gen = chromosome[random_index]
        if random_gen not in half:
            half.append(random_gen)
            half_index.append(random_index)

    return [half, half_index]


def remove_half(chromosome, half_chromosome):
    for gen in half_chromosome:
        chromosome.remove(gen)
    return chromosome


def mutation(chromosome):
    gens_count = len(chromosome)
    random_one = rd.randint(0, gens_count - 1)
    value_one = chromosome[random_one]

    random_two = rd.randint(0, gens_count - 1)
    value_two = chromosome[random_two]

    chromosome[random_one] = value_two
    chromosome[random_two] = value_one
    return chromosome

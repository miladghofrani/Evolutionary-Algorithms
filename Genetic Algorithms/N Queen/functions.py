import random as rd
from operator import itemgetter
from constants import *


def initialize_chromosomes():
    for i in range(CHROMOSOMES):
        gens = []
        blocks = [w + 1 for w in range(QUEEN)]
        for j in range(QUEEN):
            random = rd.randint(0, len(blocks)-1)
            gens.append(blocks[random])
            del blocks[random]

        chromosomes_list.append({
            "gens": gens,
            "cost": 0,
            "power": 0,
        })


def cost_of_chromosomes():
    chromosomes_cost = [chromosome["cost"] for chromosome in chromosomes_list]
    return chromosomes_cost


def roulette_wheel_method():
    power_sum = 0
    inverse_sum_cost = 0
    for chromosome in chromosomes_list:
        inverse_sum_cost += 1 / chromosome["cost"]

    for chromosome in chromosomes_list:
        inverse_cost = 1 / chromosome["cost"]
        chromosome["power"] = inverse_cost / inverse_sum_cost
        chromosome["power"] = round(chromosome["power"] * 100)
        power_sum += chromosome["power"]

    circle = []
    for i in range(len(chromosomes_list)):
        if i != 0:
            circle.append(chromosomes_list[i]["power"] + circle[i - 1])
        else:
            circle.append(chromosomes_list[i]["power"])

    return circle, power_sum


def find_parents(circle, power_sum):
    parents = set()
    while len(parents) < 2:
        random_number = rd.randint(1, power_sum)
        finding = True
        while finding:
            if random_number in circle:
                finding = False
            else:
                random_number += 1

        find_index = circle.index(random_number)
        parents.add(find_index)

    return list(parents)


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


def show_full_board(winner):
    for row in range(len(winner)):
        line = ""
        for column in range(len(winner)):
            if winner[row] == column:
                line += "♛ "
            else:
                line += ". "
        print(line)
    print("\n")

import time
from constants import *
from fitness import *
from functions import *

initialize_chromosomes()
chromosomes_cost = []

start = time.time()
T = 0
while 0 not in chromosomes_cost:
    fitness_chromosomes()
    chromosomes_cost = cost_of_chromosomes()
    if 0 in chromosomes_cost:
        break

    circle, power_sum = roulette_wheel_method()

    parents_index = find_parents(circle, power_sum)
    parent_1 = chromosomes_list[parents_index[0]]
    parent_2 = chromosomes_list[parents_index[1]]

    half_parent_1, half_parent_1_index = take_half_randomly(parent_1["gens"])
    half_parent_2 = remove_half(parent_2["gens"], half_parent_1)
    child_1 = {
        "gens": half_parent_1 + half_parent_2,
        "cost": 0,
        "power": 0,
    }
    child_2 = {
        "gens": half_parent_2 + half_parent_1,
        "cost": 0,
        "power": 0,
    }

    do_mutation = rd.randint(1, 10)
    if do_mutation > 5:
        choose_child = rd.randint(1, 10)
        if choose_child > 5:
            child_1["gens"] = mutation(child_1["gens"])
        else:
            child_2["gens"] = mutation(child_2["gens"])

    # remove parents
    chromosomes_list.remove(parent_1)
    chromosomes_list.remove(parent_2)

    # add childes to the list
    chromosomes_list.append(child_1)
    chromosomes_list.append(child_2)

    T += 1

finish = time.time()
final_index = chromosomes_cost.index(0)
print(f"Winner: {chromosomes_list[final_index]['gens']}")
print(f"Iteration: {T}")
print(f"Seconds: {round(finish - start)}")
show_full_board(chromosomes_list[final_index]["gens"])

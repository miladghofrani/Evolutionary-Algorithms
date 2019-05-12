import random as rd
from operator import itemgetter
import copy
from constants import *
from initializing import initialize_countries, initialize_empires
from fitness import get_cost, fitness_countries
from functions import cost_of_imperialist, take_half_randomly, remove_half, mutation


while len(empires) < 2:
    # Initialize countries
    initialize_countries()

    # Get cost of country
    fitness_countries()

    # Initialize empires
    initialize_empires()

imperialist_cost = cost_of_imperialist()
if 0 in imperialist_cost:
    list_of_imperialist = [empire["imperialist"] for empire in empires]
    for imperialist in list_of_imperialist:
        if imperialist["cost"] == 0:
            find = imperialist

while len(empires) > 1:
    imperialist_cost = cost_of_imperialist()
    if 0 in imperialist_cost:
        list_of_imperialist = [empire["imperialist"] for empire in empires]
        for imperialist in list_of_imperialist:
            if imperialist["cost"] == 0:
                find = imperialist
        break

    for empire in empires:
        for colony in empire["colonies"]:
            random_imperialist_block = rd.randint(0, QUEEN-1)
            random_imperialist_number = empire["imperialist"]["gens"][random_imperialist_block]
            random_colony_value = copy.deepcopy(colony["gens"][random_imperialist_block])
            random_imperialist_number_index = copy.deepcopy(colony["gens"].index(random_imperialist_number))
            colony["gens"][random_imperialist_block] = random_imperialist_number
            colony["gens"][random_imperialist_number_index] = random_colony_value
            # half_parent_1, half_parent_1_index = take_half_randomly(empire["imperialist"]["gens"])
            # half_parent_2 = remove_half(colony["gens"], half_parent_1)
            # child = half_parent_1 + half_parent_2
            # do_mutation = rd.randint(1, 10)
            # if do_mutation > 5:
            #     child = mutation(child)
            # colony["gens"] = child
            colony["cost"] = get_cost(colony["gens"])

        empire["colonies"] = sorted(empire["colonies"], key=itemgetter('cost'))
        if empire["colonies"][0]['cost'] < empire["imperialist"]["cost"]:
            temp = copy.deepcopy(empire["colonies"][0])
            empire["colonies"][0] = empire["imperialist"]
            empire["imperialist"] = temp

        colonies_cost = [colony["cost"] for colony in empire["colonies"]]
        empire["cost"] = empire["imperialist"]["cost"] + (0.5 * (sum(colonies_cost) / len(colonies_cost)))

    # Update empire normal cost
    empires_cost = [empire["cost"] for empire in empires]
    for empire in empires:
        empire["normalCost"] = abs(empire["cost"] - max(empires_cost))

    # Update empire power
    empires_normal_cost = [empire["normalCost"] for empire in empires]
    for empire in empires:
        if sum(empires_normal_cost) != 0:
            empire["power"] = empire["normalCost"] / sum(empires_normal_cost)
        else:
            empire["power"] = empire["normalCost"]

    random_uniform = []
    for i in range(len(empires)):
        random = rd.randint(0, 1)
        random_uniform.append(random)

    i = 0
    for empire in empires:
        empire["Dpower"] = empire["power"] - random_uniform[i]
        i += 1

    empires_D_power = [empire["Dpower"] for empire in empires]
    strongest_empire_index = empires_D_power.index(max(empires_D_power))
    weakest_empire_index = empires_D_power.index(min(empires_D_power))

    weakest_colonies = empires[weakest_empire_index]["colonies"]
    weakest_colony = empires[weakest_empire_index]["colonies"][len(weakest_colonies)-1]
    empires[strongest_empire_index]["colonies"].append(weakest_colony)
    del empires[weakest_empire_index]["colonies"][len(weakest_colonies)-1]

    print(" ")
    i = 0
    for empire in empires:
        if len(empire["colonies"]) == 0:
            del empires[i]
        print(len(empire["colonies"]))
        i += 1
    print(" ")

if find == 0:
    find = empires[0]["imperialist"]
print(find)

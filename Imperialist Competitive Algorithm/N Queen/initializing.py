import random as rd
from operator import itemgetter
from constants import *


def initialize_countries():
    for i in range(COUNTRIES):
        gens = []
        blocks = [w + 1 for w in range(QUEEN)]
        for j in range(QUEEN):
            random = rd.randint(0, len(blocks)-1)
            gens.append(blocks[random])
            del blocks[random]

        country_list.append({
            "gens": gens,
            "cost": 0,
            "normalCost": 0,
            "power": 0,
            "colonies": 0,
        })


def initialize_empires():
    global sorted_country_list
    global imperialist_list
    global colonies_list

    # Sort countries by cost
    sorted_country_list = sorted(country_list, key=itemgetter('cost'))

    # Take imperialists from the countries
    imperialist_list = sorted_country_list[0:IMPERIALISTS]
    # Take colonies from the countries
    colonies_list = sorted_country_list[IMPERIALISTS:]

    # Update normal cost
    imperialist_cost = [imperialist["cost"] for imperialist in imperialist_list]
    for imperialist in imperialist_list:
        imperialist["normalCost"] = abs(imperialist["cost"] - max(imperialist_cost))

    # Update power and colonies count
    imperialist_normal_cost = [imperialist["normalCost"] for imperialist in imperialist_list]
    for imperialist in imperialist_list:
        imperialist["power"] = imperialist["normalCost"] / sum(imperialist_normal_cost)
        imperialist["colonies"] = round(imperialist["power"] * COLONIES)

    # check if sum of colonies count in imperialist is more or less than all colonies
    imperialist_colonies = [imperialist["colonies"] for imperialist in imperialist_list]
    imperialist_colonies_sum = sum(imperialist_colonies)
    if imperialist_colonies_sum < COLONIES:
        left_colonies = COLONIES - imperialist_colonies_sum
        imperialist_list[0]["colonies"] = imperialist_list[0]["colonies"] + left_colonies
    if imperialist_colonies_sum > COLONIES:
        left_colonies = imperialist_colonies_sum - COLONIES
        if min(imperialist_colonies) == 0:
            zero_index = imperialist_colonies.index(0)
            imperialist_list[zero_index-1]["colonies"] = imperialist_list[zero_index-1]["colonies"] - left_colonies
        else:
            len_counts = len(imperialist_colonies)
            imperialist_list[len_counts-1]["colonies"] = imperialist_list[len_counts-1]["colonies"] - left_colonies

    counter = 0
    for imperialist in imperialist_list:
        if imperialist["colonies"] > 0:
            empires.append({
                "imperialist": imperialist,
                "colonies": colonies_list[counter:imperialist["colonies"] + counter],
                "cost": 0,
                "normalCost": 0,
                "power": 0,
                "Dpower": 0,
            })
            counter += imperialist["colonies"]

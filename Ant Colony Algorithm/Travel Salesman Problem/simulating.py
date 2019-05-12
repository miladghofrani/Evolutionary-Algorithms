from constants import *
import random as rd
import copy


# Reinitialize all ants and redistribute them
def restart_ants():
    global best_tour
    global best_index
    global best_ant
    current = 0
    for ant in range(MAX_ANTS):
        if ants[ant]["tourLength"] < best_tour:
            best_tour = copy.deepcopy(ants[ant]["tourLength"])
            best_index = copy.deepcopy(ant)
            best_ant = copy.deepcopy(ants[ant])

        ants[ant]["nextCity"] = -1
        ants[ant]["tourLength"] = 0.0

        for i in range(MAX_CITIES):
            ants[ant]["taa"][i] = 0
            ants[ant]["path"][i] = -1

        if current == MAX_CITIES:
            current = 0

        ants[ant]["curCity"] = current
        current += 1

        ants[ant]["pathIndex"] = 1
        ants[ant]["path"][0] = ants[ant]["curCity"]

        ants[ant]["taa"][ants[ant]["curCity"]] = 1
    return best_ant


def ant_product(from_city, to_city):
    # [𝜏_𝑖𝑗]^𝛼
    t = pheromone[from_city][to_city] ** ALPHA
    # 𝜼(𝒊,𝒋) = 𝟏 / 𝒅(𝒊,𝒋)
    # [𝜂_𝑖𝑗]^𝛽
    n = (1.0 / dist[from_city][to_city]) ** BETA
    return t * n


def select_next_city(ant):
    ants_product_sum = 0
    from_city = ants[ant]["curCity"]
    for to_city in range(MAX_CITIES):
        if ants[ant]["taa"][to_city] == 0:
            ants_product_sum += ant_product(from_city, to_city)

    assert ants_product_sum != 0.0

    probability_list = []
    for to_city in range(MAX_CITIES):
        if ants[ant]["taa"][to_city] == 0:
            p = ant_product(from_city, to_city) / ants_product_sum
            probability_list.append([to_city, p])

    circle = []
    for i in range(len(probability_list)):
        if i != 0:
            circle.append(probability_list[i][1] + circle[i - 1])
        else:
            circle.append(probability_list[i][1])

    random_number = rd.uniform(0.0, 1.0)
    closest = min(circle, key=lambda x: abs(x - random_number))
    closest_index = circle.index(closest)
    next_city = probability_list[closest_index][0]

    return next_city


def simulate_ants():
    moving = 0
    for ant in range(MAX_ANTS):
        # Checking if there are any more cities to visit
        if ants[ant]["pathIndex"] < MAX_CITIES:
            ants[ant]["nextCity"] = select_next_city(ant)
            ants[ant]["taa"][ants[ant]["nextCity"]] = 1
            ants[ant]["path"][ants[ant]["pathIndex"]] = ants[ant]["nextCity"]
            ants[ant]["pathIndex"] += 1
            ants[ant]["tourLength"] += dist[ants[ant]["curCity"]][ants[ant]["nextCity"]]

            # Handle last case->last city to first
            if ants[ant]["pathIndex"] == MAX_CITIES:
                ants[ant]["tourLength"] += dist[ants[ant]["path"][MAX_CITIES - 1]][ants[ant]["path"][0]]

            ants[ant]["curCity"] = ants[ant]["nextCity"]
            moving += 1
        else:
            ants[ant]["nextCity"] = ants[ant]["path"][0]
            ants[ant]["taa"][ants[ant]["nextCity"]] = 1
            ants[ant]["path"][ants[ant]["pathIndex"]] = ants[ant]["nextCity"]
            ants[ant]["pathIndex"] += 1
            ants[ant]["tourLength"] += dist[ants[ant]["path"][MAX_CITIES - 1]][ants[ant]["path"][0]]
            ants[ant]["curCity"] = ants[ant]["nextCity"]
    return moving


def update_trails():
    # Pheromone Evaporation
    for from_city in range(MAX_CITIES):
        for to_city in range(MAX_CITIES):
            if from_city != to_city:
                pheromone[from_city][to_city] *= (1.0 - RHO)
                if pheromone[from_city][to_city] < 0.0:
                    pheromone[from_city][to_city] = INIT_PHEROMONE

    # Add new pheromone to the trails
    for ant in range(MAX_ANTS):
        for i in range(MAX_CITIES):
            if i < MAX_CITIES - 1:
                from_city = ants[ant]["path"][i]
                to_city = ants[ant]["path"][i + 1]
            else:
                from_city = ants[ant]["path"][i]
                to_city = ants[ant]["path"][0]

            pheromone[from_city][to_city] += (QVAL / ants[ant]["tourLength"])
            pheromone[to_city][from_city] = pheromone[from_city][to_city]

    for from_city in range(MAX_CITIES):
        for to_city in range(MAX_CITIES):
            pheromone[from_city][to_city] *= RHO

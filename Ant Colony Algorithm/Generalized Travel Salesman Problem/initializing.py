import random as rd
import numpy as np
from constants import *


def creating_cities():
    # creating cities
    for from_city in range(MAX_CITIES):
        # randomly place cities
        lat = rd.randint(1, MAX_DIST)
        long = rd.randint(1, MAX_DIST)
        cities.append(
            {
                "lat": lat,
                "long": long,
            }
        )
        dist.append([])
        pheromone.append([])
        for to_city in range(MAX_CITIES):
            dist[from_city].append(0.0)
            pheromone[from_city].append(INIT_PHEROMONE)


def computing_distance():
    # computing distance
    for from_city in range(MAX_CITIES):
        for to_city in range(MAX_CITIES):
            if from_city != to_city and dist[from_city][to_city] == 0.0:
                xd = abs(cities[from_city]["lat"] - cities[to_city]["lat"]) ** 2
                yd = abs(cities[from_city]["long"] - cities[to_city]["long"]) ** 2

                dist[from_city][to_city] = np.sqrt(xd + yd)
                dist[to_city][from_city] = dist[from_city][to_city]


def initializing_ants():
    # initializing the ANTs
    current = 0
    for ant in range(MAX_ANTS):
        if current == MAX_CITIES:
            current = 0
        ants.append({
            "curCity": current
        })
        current += 1

        ants[ant]["taa"] = []
        ants[ant]["path"] = []
        for from_city in range(MAX_CITIES+1):
            ants[ant]["taa"].append(0)
            ants[ant]["path"].append(-1)

        ants[ant]["pathIndex"] = 1
        ants[ant]["path"][0] = ants[ant]["curCity"]
        ants[ant]["nextCity"] = -1
        ants[ant]["tourLength"] = 0

        # loading first city into taa list
        ants[ant]["taa"][ants[ant]["curCity"]] = 1
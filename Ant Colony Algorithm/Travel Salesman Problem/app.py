from constants import *
from functions import show_city_plot, show_city_with_line_plot, show_final_plot
from initializing import creating_cities, computing_distance, initializing_ants
from simulating import simulate_ants, update_trails, restart_ants

# creating cities
creating_cities()
show_city_plot(cities)
show_city_with_line_plot(cities)

# computing distance
computing_distance()

# initializing the ANTs
initializing_ants()

curTime = 0
best_final = 0
while curTime <= MAX_TIME:
    if simulate_ants() == 0:
        update_trails()
        if curTime != MAX_TIME:
            best_final = restart_ants()
        curTime += 1

# print(best_final)
ant_best = best_final
show_final_plot(ant_best, cities)

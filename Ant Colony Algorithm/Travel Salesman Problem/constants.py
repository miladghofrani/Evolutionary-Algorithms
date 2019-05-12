# Maximum number of cities that we have on the map
MAX_CITIES = 30

# Maximum pairwise distance between the cities
MAX_DIST = 100

# Worst case scenario , Max travel of Ant
MAX_TOUR = (MAX_CITIES * MAX_DIST)

# Number of ants
MAX_ANTS = 30

# Represents the importance of the trail
ALPHA = 1.0

# Relative importance of visibility
BETA = 5.0

# Represents the factor which defines the evaporation rate of the pheromones on the edges
RHO = 0.5

# Constant used in the formula
QVAL = 100

# Number of maximum tours that the ant undertakes
MAX_TOURS = 20

# Maximum time constraint in case the algorithm is not able to converge to a solution
MAX_TIME = (MAX_TOURS * MAX_CITIES)

# Weigh the edges with pheromones
INIT_PHEROMONE = (1.0 / MAX_CITIES)

# structure of city = [
#     {
#         "lat" = Latitude
#         "long" = Longitude
#     }
# ]

# structure of Ant = [
#     {
#         "curCity" = current city
#         "nextCity" = next city
#         "pathIndex" = path index
#         "taa" = [] list of cities already traversed by an Ant {Traversed Already Ant}
#         "path" = [] stores the path through which the Ant has traveled
#         "tourLength" = distance through which the ant has traveled as of the tour
#     }
# ]

cities = []
dist = []
pheromone = []
ants = []
best_tour = MAX_TOUR
best_index = 0
best_ant = 0

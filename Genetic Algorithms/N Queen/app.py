import random as rd


def menu():
    user_input = 's'

    while user_input != 'e':
        gens = int(input("What is you queen number ? "))
        count = int(input("How many sample do you need ? "))
        population_list = initialize_population(count, gens)
        fitness_list = []

        while 0 not in fitness_list:
            fitness_list = fitness_population(population_list)
            if 0 in fitness_list:
                break

            circle = ranking_method(fitness_list)

            parents_index = find_parents(circle)
            parent_1 = population_list[parents_index[0]]
            parent_2 = population_list[parents_index[1]]

            # parents_index = find_parent_minimum(fitness_list)
            # parent_1 = population_list[parents_index[0]]
            # parent_2 = population_list[parents_index[1]]

            half_parent_1, half_parent_1_index = take_half_randomly(gens, parent_1)
            half_parent_2 = remove_half(parent_2, half_parent_1)
            child_1 = half_parent_1 + half_parent_2
            child_2 = half_parent_2 + half_parent_1

            # mutation
            child_1 = mutation(child_1)
            child_2 = mutation(child_2)

            #fitness_list = only_fitness_last_two(fitness_list, parents_index[0], parents_index[1], child_1, child_2)
            #if 0 in fitness_list:
                #break

            # remove parents
            population_list.remove(parent_1)
            population_list.remove(parent_2)

            # add childes to the list
            population_list.append(child_1)
            population_list.append(child_2)


        final_index = fitness_list.index(0)
        print(population_list[final_index])

        user_input = input("\nStart again 's'\nExit 'e'\nWrite your command: ").strip()


def initialize_population(count, gens):
    population_list = []
    for i in range(count):
        x = []
        blocks = [w + 1 for w in range(gens)]
        for j in range(gens):
            random = rd.randint(0, len(blocks)-1)
            x.append(blocks[random])
            del blocks[random]

        population_list.append(x)

    return population_list


def fitness_chromosome(chromosome):
    error = 0
    columns = [i + 1 for i in range(len(chromosome))]
    rows = [j + 1 for j in range(len(chromosome))]

    for column in columns:
        for row in rows:
            if column != row:
                if chromosome[column-1] == chromosome[row-1]:
                    error += 1
                if abs(column - row) == abs(chromosome[column-1] - chromosome[row-1]):
                    error += 1
    return error


def fitness_population(population_list):
    fitness_list = []
    for chromosome in population_list:
        fc = fitness_chromosome(chromosome)
        fitness_list.append(fc)
    return fitness_list


def only_fitness_last_two(fitness_list, parent_index_1, parent_index_2, child_1, child_2):
    new_fitness_list = [fitness_list[i] for i in range(len(fitness_list)) if i != parent_index_1 and i != parent_index_2]

    fc_child_1 = fitness_chromosome(child_1)
    fc_child_2 = fitness_chromosome(child_2)

    new_fitness_list.append(fc_child_1)
    new_fitness_list.append(fc_child_2)

    return new_fitness_list


def ranking_method(fitness_list):
    # fitness_list = list(dict.fromkeys(fitness_list))
    fitness_list.sort()
    fitness_list.reverse()

    rank_list = [i + 1 for i in range(len(fitness_list))]
    rank_of_numbers = []
    for rank in rank_list:
        rank_of_numbers.append(round(rank / sum(rank_list) * 100))

    circle = []
    for i in range(len(rank_of_numbers)):
        if i != 0:
            circle.append(rank_of_numbers[i] + circle[i - 1])
        else:
            circle.append(rank_of_numbers[i])

    return circle


def find_parents(circle):
    parents = set()
    while len(parents) < 2:
        random_number = rd.randint(1, 100)
        closest = min(circle, key=lambda x: abs(x - random_number))

        if closest == 100:
            parents.add(len(circle) - 1)
        if closest == 1:
            parents.add(0)

        closest_index = circle.index(closest)
        if random_number >= closest:
            if closest_index < len(circle) - 1:
                find_index = closest_index + 1
            else:
                find_index = closest_index
            parents.add(find_index)
        else:
            parents.add(closest_index)

    return list(parents)


def find_parent_minimum(fitness_list):
    copy_fitness_list = fitness_list.copy()
    copy_fitness_list.sort()
    fit_1 = copy_fitness_list[0]
    fit_2 = copy_fitness_list[1]
    fit_index_1 = fitness_list.index(fit_1)
    if fit_1 == fit_2:
        fit_index_2 = fitness_list.index(fit_2, fit_index_1 + 1)
    else:
        fit_index_2 = fitness_list.index(fit_2)

    return [fit_index_1, fit_index_2]


def take_half_randomly(gens, chromosome):
    half_gens = gens//2
    half = []
    half_index = []
    while len(half) < half_gens:
        random_index = rd.randint(0, gens-1)
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


menu()
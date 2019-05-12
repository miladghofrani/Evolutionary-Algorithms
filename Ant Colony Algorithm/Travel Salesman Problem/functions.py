import matplotlib.pyplot as plt


def show_city_plot(cities):
    f1 = plt.figure(1)
    latitudes = [city["lat"] for city in cities]
    longitudes = [city["long"] for city in cities]
    plt.scatter(latitudes, longitudes, color="m", marker="o", s=30)
    plt.xlabel("Latitude")
    plt.ylabel('Longitude')
    # plt.show()


def show_city_with_line_plot(cities):
    f2 = plt.figure(2)
    latitudes = [city["lat"] for city in cities]
    longitudes = [city["long"] for city in cities]
    for i in range(len(latitudes)):
        for j in range(len(longitudes)):
            plt.plot([latitudes[i], latitudes[j]], [longitudes[i], longitudes[j]], marker='o', linestyle='--', color='k', markerfacecolor='m')
    plt.xlabel("Latitude")
    plt.ylabel('Longitude')
    # plt.show()


def show_final_plot(ant_best, cities):
    f3 = plt.figure(3)
    city_index_list = [city for city in ant_best["path"]]
    final_cities = [cities[i] for i in city_index_list]
    x = [x["lat"] for x in final_cities]
    y = [y["long"] for y in final_cities]
    plt.plot(x, y, marker='o', linestyle='--', color='k', markerfacecolor='m')
    # Start Green color
    plt.plot(x[0:2], y[0:2], marker='o', linestyle='--', color='g', markerfacecolor='g')
    # End Red color
    plt.plot(x[len(x)-2:], y[len(y)-2:], marker='o', linestyle='--', color='r', markerfacecolor='r')
    # Start point
    plt.plot(x[0], y[0], marker='o', linestyle='--', color='c', markerfacecolor='c')
    for i in range(len(city_index_list)):
        plt.text(final_cities[i]["lat"], final_cities[i]["long"], city_index_list[i])

    plt.xlabel("Latitude")
    plt.ylabel('Longitude')
    plt.show()

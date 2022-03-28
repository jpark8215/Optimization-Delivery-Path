
# This file takes data from the distance csv file, creates vertices based on the name of the location,
# and graphs the data using undirected edges. Each edge has a weight that represents the miles between each vertex
from datetime import datetime

import distance
import hash
import package
import truck

first_optimized_truck = []
first_optimized_truck_index_list = []

second_optimized_truck = []
second_optimized_truck_index_list = []

third_optimized_truck = []
third_optimized_truck_index_list = []


def get_minimum_distance(truck_route_list, truck_number, current_location):
    if not truck_route_list:
        return truck_route_list

    index = 0
    dist_list = []
    minimum = 0

    for index, outer in enumerate(truck_route_list):
        for inner in distance.get_address():
            if outer == inner[1]:
                dist = distance.get_distance(current_location, int(inner[0]))
                dist_list.append(dist)
                minimum = float(min(dist_list))

    index += 1

    return minimum


# get route from Truck and optimize the route using nearest
def get_shortest_route(truck_route_list, truck_number, current_location):
    if not len(truck_route_list):
        return truck_route_list

    index = 0

    for index, outer in enumerate(truck_route_list):
        for inner in distance.get_address():
            if outer == inner[1]:
                dist = distance.get_distance(current_location, int(inner[0]))
                shortest_distance = get_minimum_distance(truck_route_list, truck_number, current_location)

                if dist == shortest_distance:
                    if truck_number == 1:
                        first_optimized_truck_index_list.append(inner[0])
                        first_optimized_truck.append(inner[1])
                        truck_route_list.remove(inner[1])
                        get_shortest_route(truck_route_list, truck_number, current_location)

                    elif truck_number == 2:
                        second_optimized_truck_index_list.append(inner[0])
                        second_optimized_truck.append(inner[1])
                        truck_route_list.remove(inner[1])
                        get_shortest_route(truck_route_list, truck_number, current_location)

                    elif truck_number == 3:
                        third_optimized_truck_index_list.append(inner[0])
                        third_optimized_truck.append(inner[1])
                        truck_route_list.remove(inner[1])
                        get_shortest_route(truck_route_list, truck_number, current_location)

    index += 1
    # return first_optimized_truck


get_shortest_route(truck.truck1.route, 1, 0)


def first_truck_list():
    return first_optimized_truck


# Insert 0 for the first index of each index list
first_optimized_truck_index_list.insert(0, '0')


# The following are all helper functions to return a desired value -> O(1)
def first_truck_index():
    return first_optimized_truck_index_list


get_shortest_route(truck.truck2.route, 2, 0)


def second_truck_list():
    return second_optimized_truck


# Insert 0 for the first index of each index list
second_optimized_truck_index_list.insert(0, '0')


# The following are all helper functions to return a desired value -> O(1)
def second_truck_index():
    return second_optimized_truck_index_list


get_shortest_route(truck.truck3.route, 3, 0)


def third_truck_list():
    return third_optimized_truck


# Insert 0 for the first index of each index list
third_optimized_truck_index_list.insert(0, '0')


# The following are all helper functions to return a desired value -> O(1)
def third_truck_index():
    return third_optimized_truck_index_list


# Empty lists created
first_delivery = []
second_delivery = []
third_delivery = []

first_truck_packages = []
second_truck_packages = []
third_truck_packages = []

# Times the trucks leave the hub
first_leave_times = ['8:00:00']
second_leave_times = ['9:05:00']
third_leave_times = ['10:00:00']


# Set delivery_start to first_leave_time for all truck one packages -> O(n)
def deliver_packages():
    total_distance_1 = 0
    delivered_time = None

    for outer in first_optimized_truck:
        for index, inner in enumerate(truck.truck1.packages_loaded):
            if outer == inner[1]:
                truck.truck1.packages_loaded[index][8] = first_leave_times[0]
                first_delivery.append(truck.truck1.packages_loaded[index])

    # Compare truck one addresses to address list -> O(n^2)
    for index, outer in enumerate(first_delivery):
        for inner in distance.get_address():
            if outer[1] == inner[1]:
                first_truck_packages.append(outer[0])
                first_delivery[index][1] = inner[0]

    # Calculate total distance of the first truck and distance of each package -> O(n)
    for index in range(len(first_optimized_truck_index_list) - 1):
        total_distance_1 = distance.get_total_distance(int(first_optimized_truck_index_list[index]),
                                                       int(first_optimized_truck_index_list[index + 1]),
                                                       total_distance_1)
        delivered_time = distance.get_time(total_distance_1, first_delivery)

    return total_distance_1, delivered_time

# deliver_packages()
# first_delivery[index][10] = str(deliver_packages().index(1))
# package.package_hash.update(int(first_delivery[0]), first_delivery)









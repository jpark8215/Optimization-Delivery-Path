# This file takes data from the distance csv file, creates vertices based on the name of the location,
# and graphs the data using undirected edges. Each edge has a weight that represents the miles between each vertex
from datetime import datetime

import distance
import hash
import package
import truck

first_optimized_truck_address = []
first_optimized_truck_index_list = []
second_optimized_truck_address = []
second_optimized_truck_index_list = []
third_optimized_truck_address = []
third_optimized_truck_index_list = []


def get_minimum_distance(truck_route_list, truck_number, current_location):
    if not truck_route_list:
        return truck_route_list

    route_list_index = 0
    dist_list = []
    minimum = 0

    for route_list_index, outer in enumerate(truck_route_list):
        for inner in distance.get_address():
            if outer == inner[1]:
                dist = distance.get_distance(current_location, int(inner[0]))
                dist_list.append(dist)
                minimum = float(min(dist_list))

    route_list_index += 1

    return minimum


# get route from Truck and optimize the route using nearest
def get_shortest_route(truck_route_list, truck_number, current_location):
    if not len(truck_route_list):
        return truck_route_list

    route_list_index = 0

    for route_list_index, outer in enumerate(truck_route_list):
        for inner in distance.get_address():
            if outer == inner[1]:
                dist = distance.get_distance(current_location, int(inner[0]))
                shortest_distance = get_minimum_distance(truck_route_list, truck_number, current_location)

                if dist == shortest_distance:
                    if truck_number == 1:
                        first_optimized_truck_index_list.append(inner[0])
                        first_optimized_truck_address.append(inner[1])
                        truck_route_list.remove(inner[1])
                        get_shortest_route(truck_route_list, truck_number, current_location)

                    elif truck_number == 2:
                        second_optimized_truck_index_list.append(inner[0])
                        second_optimized_truck_address.append(inner[1])
                        truck_route_list.remove(inner[1])
                        get_shortest_route(truck_route_list, truck_number, current_location)

                    elif truck_number == 3:
                        third_optimized_truck_index_list.append(inner[0])
                        third_optimized_truck_address.append(inner[1])
                        truck_route_list.remove(inner[1])
                        get_shortest_route(truck_route_list, truck_number, current_location)

    route_list_index += 1


# Empty lists created
first_optimized_packages_list = []
second_optimized_packages_list = []
third_optimized_packages_list = []


def get_optimized_package_list(optimized_truck_address, truck_packages, optimized_packages_list):

    for location_index in enumerate(optimized_truck_address):
        for package_index, value in enumerate(truck_packages):
            if location_index[1] == value[1]:
                optimized_packages_list.append(truck_packages[package_index])
                truck_packages.pop(package_index)

    return optimized_packages_list


# Set delivery_start to first_leave_time for all truck one packages -> O(n)
for index, value in enumerate(truck.truck1.packages_loaded):
    truck.truck1.start_delivery('8:00:00')
    truck.truck1.packages_loaded[index][8] = truck.truck1.start_time

for index, value in enumerate(truck.truck2.packages_loaded):
    truck.truck2.start_delivery('9:05:00')
    truck.truck2.packages_loaded[index][8] = truck.truck2.start_time

for index, value in enumerate(truck.truck3.packages_loaded):
    truck.truck3.start_delivery('10:00:00')
    truck.truck3.packages_loaded[index][8] = truck.truck3.start_time


get_shortest_route(truck.truck1.route, 1, 0)

get_optimized_package_list(first_optimized_truck_address, truck.truck1.packages_loaded, first_optimized_packages_list)

# Insert 0 for the first index of each index list
first_optimized_truck_index_list.insert(0, '0')
first_optimized_truck_index_list.append('0')

get_shortest_route(truck.truck2.route, 2, 0)

get_optimized_package_list(second_optimized_truck_address, truck.truck2.packages_loaded, second_optimized_packages_list)

# Insert 0 for the first index of each index list
second_optimized_truck_index_list.insert(0, '0')
second_optimized_truck_index_list.append('0')

get_shortest_route(truck.truck3.route, 3, 0)

get_optimized_package_list(third_optimized_truck_address, truck.truck3.packages_loaded, third_optimized_packages_list)

# Insert 0 for the first index of each index list
third_optimized_truck_index_list.insert(0, '0')
third_optimized_truck_index_list.append('0')


first_truck_total_distance = 0

for i in range(len(first_optimized_truck_index_list) - 1):
    # calculate the total distance of the truck
    first_truck_total_distance = distance.get_total_distance(int(first_optimized_truck_index_list[i]),
                                                             int(first_optimized_truck_index_list[i + 1]),
                                                             first_truck_total_distance)
    delivered_time = distance.get_time(first_truck_total_distance)

    first_optimized_packages_list[i][10] = str(delivered_time)
    if i == int(len(first_optimized_truck_index_list) - 1):
        return_to_hub_time = delivered_time
        truck.truck1.back_to_hub(return_to_hub_time)
    package.package_hash.update(int(first_optimized_packages_list[i][0]), first_optimized_packages_list)



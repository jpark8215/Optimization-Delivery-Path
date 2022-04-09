import time

import distance
import package
import truck

'''
SET first_optimized_truck_address TO []
SET first_optimized_truck_index_list TO []
SET second_optimized_truck_address TO []
SET second_optimized_truck_index_list TO []
SET third_optimized_truck_address TO []
SET third_optimized_truck_index_list TO []

DEFINE FUNCTION convert_to_time(t):
    SET dt_obj TO time.strptime(t, "%H:%M:%S")
    RETURN dt_obj

DEFINE FUNCTION get_minimum_distance(truck_route_list, truck_number, current_location):
    SET route_list_index TO 0
    SET distance_list TO []
    SET minimum TO 0

    FOR route_list_index, outer IN enumerate(truck_route_list):
        FOR inner IN distance.get_address():
            IF outer EQUALS inner[1]:
                SET dist TO distance.get_distance(current_location, int(inner[0]))
                distance_list.append(dist)
                SET minimum TO float(min(distance_list))
    route_list_index += 1
    RETURN minimum

DEFINE FUNCTION get_shortest_route(truck_route_list, truck_number, current_location):
    SET route_list_index TO 0
    FOR route_list_index, outer IN enumerate(truck_route_list):
        FOR inner IN distance.get_address():
            IF outer EQUALS inner[1]:
                SET dist TO distance.get_distance(current_location, int(inner[0]))
                SET shortest_distance TO get_minimum_distance(truck_route_list, truck_number, current_location)

                IF dist EQUALS shortest_distance:
                    IF truck_number EQUALS 1:
                        first_optimized_truck_index_list.append(inner[0])
                        first_optimized_truck_address.append(inner[1])
                        truck_route_list.remove(inner[1])
                        get_shortest_route(truck_route_list, truck_number, current_location)

                    ELSEIF truck_number EQUALS 2:
                        second_optimized_truck_index_list.append(inner[0])
                        second_optimized_truck_address.append(inner[1])
                        truck_route_list.remove(inner[1])
                        get_shortest_route(truck_route_list, truck_number, current_location)

                    ELSEIF truck_number EQUALS 3:
                        third_optimized_truck_index_list.append(inner[0])
                        third_optimized_truck_address.append(inner[1])
                        truck_route_list.remove(inner[1])
                        get_shortest_route(truck_route_list, truck_number, current_location)

    route_list_index += 1

SET first_optimized_packages_list TO []
SET second_optimized_packages_list TO []
SET third_optimized_packages_list TO []

DEFINE FUNCTION get_optimized_package_list(optimized_truck_address, truck_packages, optimized_packages_list):
    FOR location_index IN enumerate(optimized_truck_address):
        FOR package_index, value IN enumerate(truck_packages):
        
            IF location_index[1] EQUALS value[1]:
                optimized_packages_list.append(truck_packages[package_index])
                truck_packages.pop(package_index)
    RETURN optimized_packages_list

FOR index, value IN enumerate(truck.truck1.packages_loaded):
    truck.truck1.start_delivery('8:00:00')
    SET truck.truck1.packages_loaded[index][8] TO truck.truck1.start_time

FOR index, value IN enumerate(truck.truck2.packages_loaded):
    truck.truck2.start_delivery('9:05:00')
    SET truck.truck2.packages_loaded[index][8] TO truck.truck2.start_time

FOR index, value IN enumerate(truck.truck3.packages_loaded):
    truck.truck3.start_delivery('10:32:40'
    SET truck.truck3.packages_loaded[index][8] TO truck.truck3.start_time


get_shortest_route(truck.truck1.route, 1, 0)
get_optimized_package_list(first_optimized_truck_address, truck.truck1.packages_loaded, first_optimized_packages_list)

first_optimized_truck_index_list.insert(0, '0')
first_optimized_truck_index_list.append('0')


get_shortest_route(truck.truck2.route, 2, 0)
get_optimized_package_list(second_optimized_truck_address, truck.truck2.packages_loaded, second_optimized_packages_list)

second_optimized_truck_index_list.insert(0, '0')
second_optimized_truck_index_list.append('0')


get_shortest_route(truck.truck3.route, 3, 0)
get_optimized_package_list(third_optimized_truck_address, truck.truck3.packages_loaded, third_optimized_packages_list)

third_optimized_truck_index_list.insert(0, '0')
third_optimized_truck_index_list.append('0')


DEFINE FUNCTION get_distance_and_time(optimized_truck_index_list, optimized_packages_list_time):
    SET truck_total_distance TO 0
    SET delivery_total_distance TO 0

    FOR i IN range(len(optimized_packages_list_time)):
        IF optimized_packages_list_time[i][9] EQUALS '':
            SET optimized_packages_list_time[i][9] TO '0:00:00'

        IF optimized_packages_list_time[i][10] EQUALS '':
            SET optimized_packages_list_time[i][10] TO '0:00:00'

    FOR i IN range(len(optimized_truck_index_list) - 1):
        SET truck_total_distance TO distance.get_total_distance(int(optimized_truck_index_list[i]),
                                                           int(optimized_truck_index_list[i + 1]),
                                                           truck_total_distance)
        SET delivered_time TO distance.get_time(truck_total_distance, optimized_packages_list_time)

        IF i < int(len(optimized_truck_index_list) - 2):
            SET delivery_total_distance TO truck_total_distance
            SET optimized_packages_list_time[i][10] TO str(delivered_time)
            # package.package_hash.update(int(optimized_packages_list_time[i][0]), optimized_packages_list_time)

        ELSEIF i EQUALS int(len(optimized_truck_index_list) - 1):
            SET optimized_packages_list_time[i][9] TO str(delivered_time)
            # package.package_hash.update(int(optimized_packages_list_time[i][0]), optimized_packages_list_time)

        FOR i IN range(len(optimized_truck_index_list) - 2):
            SET optimized_packages_list_time[i][9] TO str(delivered_time)
            # package.package_hash.update(int(optimized_packages_list_time[i][0]), optimized_packages_list_time)

    RETURN delivery_total_distance


DEFINE FUNCTION first_truck_distance():
    SET truck_one_distance TO get_distance_and_time(first_optimized_truck_index_list, first_optimized_packages_list)
    RETURN truck_one_distance

DEFINE FUNCTION second_truck_distance():
    SET truck_two_distance TO get_distance_and_time(second_optimized_truck_index_list, second_optimized_packages_list)
    RETURN truck_two_distance

DEFINE FUNCTION third_truck_distance():
    SET truck_three_distance TO get_distance_and_time(third_optimized_truck_index_list, third_optimized_packages_list)
    RETURN truck_three_distance

DEFINE FUNCTION get_overall_distance():
    SET overall_distance TO first_truck_distance() + second_truck_distance() + third_truck_distance()
    RETURN overall_distance


DEFINE FUNCTION update_packages_status(t, optimized_packages_list_status):
    FOR i IN range(len(optimized_packages_list_status)):
        IF convert_to_time(optimized_packages_list_status[i][8]) >= convert_to_time(t):
            optimized_packages_list_status[i].append('At hub')
            # package.package_hash.update(int(optimized_packages_list_status[i][0]), optimized_packages_list_status)

        ELSEIF convert_to_time(optimized_packages_list_status[i][10]) < convert_to_time(t):
            optimized_packages_list_status[i].append('Delivered')
            # package.package_hash.update(int(optimized_packages_list_status[i][0]), optimized_packages_list_status)

        ELSE:
            optimized_packages_list_status[i].append('En route')
            # package.package_hash.update(int(optimized_packages_list_status[i][0]), optimized_packages_list_status)

    RETURN optimized_packages_list_status

SET status_updated_list TO []

DEFINE FUNCTION get_status(t):
    status_updated_list.append(update_packages_status(t, first_optimized_packages_list))
    status_updated_list.append(update_packages_status(t, second_optimized_packages_list))
    status_updated_list.append(update_packages_status(t, third_optimized_packages_list))
    
    RETURN status_updated_list
'''
# Empty lists of optimized addresses and index lists for each truck
first_optimized_truck_address = []
first_optimized_truck_index_list = []
second_optimized_truck_address = []
second_optimized_truck_index_list = []
third_optimized_truck_address = []
third_optimized_truck_index_list = []


# O(1)
# Converts string to time
def convert_to_time(t):
    dt_obj = time.strptime(t, "%H:%M:%S")
    return dt_obj


# O(N2)
# Gets list of locations from each truck from truck.py and adds them to list
# Returns smallest number from list
def get_minimum_distance(truck_route_list, truck_number, current_location):
    route_list_index = 0
    distance_list = []
    minimum = 0

    for route_list_index, outer in enumerate(truck_route_list):
        for inner in distance.get_address():
            if outer == inner[1]:
                dist = distance.get_distance(current_location, int(inner[0]))
                distance_list.append(dist)
                minimum = float(min(distance_list))
    route_list_index += 1
    return minimum


# O(N2)
# Gets list of locations from truck.py for each truck
# Optimizes route using nearest neighbor algorithm and greedy algorithm
def get_shortest_route(truck_route_list, truck_number, current_location):
    route_list_index = 0

    # Compares truck routes distance starting shortest route in list
    for route_list_index, outer in enumerate(truck_route_list):
        for inner in distance.get_address():
            if outer == inner[1]:
                dist = distance.get_distance(current_location, int(inner[0]))
                shortest_distance = get_minimum_distance(truck_route_list, truck_number, current_location)

                # Adds optimized route index and address to lists
                # Removes data from truck route list when added to optimized list
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


# Empty list of optimized route packages
first_optimized_packages_list = []
second_optimized_packages_list = []
third_optimized_packages_list = []


# O(N2)
# Compares optimized address list with truck package list from truck.py
# Adds packages to optimized packages list and pops added package from truck package list
def get_optimized_package_list(optimized_truck_address, truck_packages, optimized_packages_list):
    for location_index in enumerate(optimized_truck_address):
        for package_index, value in enumerate(truck_packages):
            if location_index[1] == value[1]:
                optimized_packages_list.append(truck_packages[package_index])
                truck_packages.pop(package_index)

    return optimized_packages_list


# O(N)
# Sets start delivery time to truck one and updates truck package start time
for index, value in enumerate(truck.truck1.packages_loaded):
    truck.truck1.start_delivery('8:00:00')
    truck.truck1.packages_loaded[index][8] = truck.truck1.start_time

# O(N)
# Sets start delivery time to truck two and updates truck package start time
for index, value in enumerate(truck.truck2.packages_loaded):
    truck.truck2.start_delivery('9:05:00')
    truck.truck2.packages_loaded[index][8] = truck.truck2.start_time

# O(N)
# Sets start delivery time to truck three and updates truck package start time
for index, value in enumerate(truck.truck3.packages_loaded):
    truck.truck3.start_delivery('10:32:40')
    truck.truck3.packages_loaded[index][8] = truck.truck3.start_time

# Runs shortest route algorithm for truck one
get_shortest_route(truck.truck1.route, 1, 0)
# Optimizes package list for truck one
get_optimized_package_list(first_optimized_truck_address, truck.truck1.packages_loaded, first_optimized_packages_list)

# Insert 0 to index list as truck leaves and returns to hub
first_optimized_truck_index_list.insert(0, '0')
first_optimized_truck_index_list.append('0')

# Runs shortest route algorithm for truck two
get_shortest_route(truck.truck2.route, 2, 0)
# Optimizes package list for truck two
get_optimized_package_list(second_optimized_truck_address, truck.truck2.packages_loaded, second_optimized_packages_list)

# Insert 0 to index list as truck leaves and returns to hub
second_optimized_truck_index_list.insert(0, '0')
second_optimized_truck_index_list.append('0')

# Runs shortest route algorithm for truck three
get_shortest_route(truck.truck3.route, 3, 0)
# Optimizes package list for truck three
get_optimized_package_list(third_optimized_truck_address, truck.truck3.packages_loaded, third_optimized_packages_list)

# Insert 0 to index list as truck leaves and returns to hub
third_optimized_truck_index_list.insert(0, '0')
third_optimized_truck_index_list.append('0')


# O(N2)
# Gets distance and time using optimized truck location index and optimized package lists
# truck_total_distance returns total distance hub to hub
# Delivery_total_distance returns distance hub to last delivery
def get_distance_and_time(optimized_truck_index_list, optimized_packages_list_time):
    truck_total_distance = 0
    delivery_total_distance = 0

    # Replaces empty string to time format for comparison
    for i in range(len(optimized_packages_list_time)):
        if optimized_packages_list_time[i][9] == '':
            optimized_packages_list_time[i][9] = '0:00:00'
        if optimized_packages_list_time[i][10] == '':
            optimized_packages_list_time[i][10] = '0:00:00'

    # Gets distance from current location to next
    # Calculates total distance of truck and delivery time for each delivery location from distance.py
    for i in range(len(optimized_truck_index_list) - 1):
        truck_total_distance = distance.get_total_distance(int(optimized_truck_index_list[i]),
                                                           int(optimized_truck_index_list[i + 1]),
                                                           truck_total_distance)
        delivered_time = distance.get_time(truck_total_distance, optimized_packages_list_time)

        # Gets delivery time for each location and adds it to optimized package list
        if i < int(len(optimized_truck_index_list) - 2):
            delivery_total_distance = truck_total_distance
            optimized_packages_list_time[i][10] = str(delivered_time)
            # package.package_hash.update(int(optimized_packages_list_time[i][0]), optimized_packages_list_time)

        # Gets return to hub time and adds it to optimized package list
        elif i == int(len(optimized_truck_index_list) - 1):
            optimized_packages_list_time[i][9] = str(delivered_time)
            # package.package_hash.update(int(optimized_packages_list_time[i][0]), optimized_packages_list_time)

        # Updates current location time and adds it to optimized package list as truck travels
        for i in range(len(optimized_truck_index_list) - 2):
            optimized_packages_list_time[i][9] = str(delivered_time)
            # package.package_hash.update(int(optimized_packages_list_time[i][0]), optimized_packages_list_time)

    return delivery_total_distance


# O(1)
# Returns total distance for first truck and adds time to list
def first_truck_distance():
    truck_one_distance = get_distance_and_time(first_optimized_truck_index_list, first_optimized_packages_list)
    return truck_one_distance


# O(1)
# Returns total distance for second truck and adds time to list
def second_truck_distance():
    truck_two_distance = get_distance_and_time(second_optimized_truck_index_list, second_optimized_packages_list)
    return truck_two_distance


# O(1)
# Returns total distance for third truck and adds time to list
def third_truck_distance():
    truck_three_distance = get_distance_and_time(third_optimized_truck_index_list, third_optimized_packages_list)
    return truck_three_distance


# O(1)
# Gets overall distance for all three trucks
def get_overall_distance():
    overall_distance = first_truck_distance() + second_truck_distance() + third_truck_distance()
    return overall_distance


# O(N)
# Updates package status at a given time and updates optimized package list
def update_packages_status(t, optimized_packages_list_status):
    for i in range(len(optimized_packages_list_status)):
        if convert_to_time(optimized_packages_list_status[i][8]) >= convert_to_time(t):
            optimized_packages_list_status[i].append('At hub')
            # package.package_hash.update(int(optimized_packages_list_status[i][0]), optimized_packages_list_status)
        elif convert_to_time(optimized_packages_list_status[i][10]) < convert_to_time(t):
            optimized_packages_list_status[i].append('Delivered')
            # package.package_hash.update(int(optimized_packages_list_status[i][0]), optimized_packages_list_status)
        else:
            optimized_packages_list_status[i].append('En route')
            # package.package_hash.update(int(optimized_packages_list_status[i][0]), optimized_packages_list_status)
    return optimized_packages_list_status


# Empty package list that will have status of packages
status_updated_list = []


# O(1)
# Gets updated package status and adds it to list
# Returns updated list for all truck packages
def get_status(t):
    status_updated_list.append(update_packages_status(t, first_optimized_packages_list))
    status_updated_list.append(update_packages_status(t, second_optimized_packages_list))
    status_updated_list.append(update_packages_status(t, third_optimized_packages_list))
    return status_updated_list

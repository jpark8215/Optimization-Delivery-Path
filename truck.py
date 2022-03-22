
# The Truck Class assists in creating truck objects which will be loaded with packages
import csv

import distance
import greedy
import hash
import package


class Truck:

    # Constructor to initialize packages on the truck, route, delivery start time, and mileage
    def __init__(self):
        self.packages_loaded = []
        self.route = []
        self.start_time = None
        self.delivery_time = None
        self.finish_time = None
        self.speed = 0.3  # 18mph is equivalent to 0.3 miles / minute

    # Put package on truck
    def insert(self, p):
        self.packages_loaded.append(p)  # puts the package onto the truck
        self.route.append(p[1])  # package[1] == street address where the package is going

    # Delivered packages are removed from the truck
    def remove(self, p):
        self.packages_loaded.remove(p)  # takes the package off the truck
        self.route.remove(p[1])  # removes the address from the route

    # Leave the hub and start the delivery route
    def start_delivery(self, time):
        self.start_time = time

    # This is updated as deliveries are made
    def current_time(self, time):
        self.delivery_time = time
        return time

    # Time that the truck finished their deliveries and is back at the hub
    # This will tell truck 3 when to leave (as there are only 2 drivers)
    def returned_to_hub(self, time):
        self.finish_time = time
        return time


# Create truck objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()


# these lists represent the sorted trucks that are put in order of efficiency in the function below
first_optimized_truck = []
first_optimized_truck_index_list = []
second_optimized_truck = []
second_optimized_truck_index_list = []
third_optimized_truck = []
third_optimized_truck_index_list = []
first_truck_distances = []
second_truck_distances = []
third_truck_distances = []
# Times the trucks leave the hub
first_leave_times = ['8:00:00']
second_leave_times = ['9:15:00']
third_leave_times = ['10:30:00']


# This is my sorting algorithm that uses a greedy approach to automate optimizing the delivery route for each truck.
# the function takes 3 parameters (see section 1)
# First parameter is the list of packages on a truck that has not been optimized yet
# The second parameter represents the truck number
# The third parameter represents the current location that is updated each time a truck moves

# The base case of the algorithm is stated in the initial if statement (see section 2). This breaks the recursion
# once the input list has a size of 0.
# It starts by setting a "lowest value" of 50.0 and then uses the check current distance function to loop through
# every possible point that is currently available to see if there is a lower value. If there is than the lowest
# value is updated and the search continues (see section 3). Once it has searched through all possible routes
# the truck can go given the available packages, it then adds that package object and associated index to
# new lists (see section 4). To ensure that the right truck packages are being associated, the second parameter
# is checked. If the truck truck is being sorted than the optimized delivery path will be associated to the lists
# first_optimized_truck and first_optimized_truck_index. Each time these lists are updated, the lowest value is
# removed from the argument list, truck_distance_list. This will allow us to update current location and recursively
# call the function. Once the argument list is empty it will return the empty list and the function call will end.

# The space-time complexity of this algorithm is O(N^2). This is due to the two for loops and the repeated lookup
# functionality required to determine the lowest possible path then move the truck to that position.

def get_shortest_route(distance_list, truck_number, current_location):
    if not len(distance_list):
        return distance_list
    # print(address_list)

    lowest_value = 25.0
    new_location = 0

    for distance_list_index in distance_list:
        # value = int(i[1])
        if distance.get_distance(current_location, int(distance_list_index[0])) <= lowest_value:
            lowest_value = distance.get_distance(current_location, int(distance_list_index[0]))
            new_location = int(distance_list_index[0])

    for distance_list_index in distance_list:
        if distance.get_distance(current_location, int(distance_list_index[0])) == lowest_value:
            if truck_number == 1:
                first_optimized_truck.append(distance_list_index)
                first_optimized_truck_index_list.append(distance_list_index[0])
                distance_list.pop(distance_list.index(distance_list_index))
                current_location = new_location
                get_shortest_route(distance_list, 1, current_location)
            elif truck_number == 2:
                second_optimized_truck.append(distance_list_index)
                second_optimized_truck_index_list.append(distance_list_index[0])
                distance_list.pop(distance_list.index(distance_list_index))
                current_location = new_location
                get_shortest_route(distance_list, 2, current_location)
            elif truck_number == 3:
                third_optimized_truck.append(distance_list_index)
                third_optimized_truck_index_list.append(distance_list_index[0])
                distance_list.pop(distance_list.index(distance_list_index))
                current_location = new_location
                get_shortest_route(distance_list, 3, current_location)


# Insert 0 for the first index of each index list
first_optimized_truck_index_list.insert(0, '0')
second_optimized_truck_index_list.insert(0, '0')
third_optimized_truck_index_list.insert(0, '0')


def first_truck_route():
    for index, outer in enumerate(truck1.packages_loaded):
        for inner in distance.get_address():
            if outer[1] == inner[2]:
                first_truck_distances.append(outer[0])
                truck1.packages_loaded[index][1] = inner[0]

    # Call algorithm to sort packages for first truck
    return get_shortest_route(truck1.route, 1, 0)


# The following are all helper functions to return a desired value -> O(1)
def first_truck_index():
    return first_optimized_truck_index_list


def first_truck_list():
    return first_optimized_truck


def first_truck_distance():
    # Call algorithm to sort packages for first truck
    first_truck_list()
    total_distance_1 = 0

    # Calculate total distance of the first truck and distance of each package -> O(n)
    for index in range(len(first_truck_index())):
        try:
            total_distance_1 = distance.get_total_distance(int(first_truck_index()[index]), int(first_truck_index()[index + 1]), total_distance_1)
            deliver_package = distance.get_time(distance.get_distance(int(first_truck_index()[index]), int(first_truck_index()[index + 1])), first_leave_times)
            truck1.packages_loaded[index][10] = (str(deliver_package))
            hash.ChainingHashTable.update(truck1.packages_loaded[index][0], truck1.packages_loaded, deliver_package)
        except IndexError:
            pass

    return total_distance_1


def second_truck_route():
    for index, outer in enumerate(truck2.packages_loaded):
        for inner in distance.get_address():
            if outer[1] == inner[1]:
                second_truck_distances.append(outer[0])
                truck2.packages_loaded[index][1] = inner[0]

    # Call algorithm to sort packages for first truck
    return get_shortest_route(truck2.route, 2, 0)


def second_truck_index():
    return second_optimized_truck_index_list


def second_truck_list():
    return second_optimized_truck


def second_truck_distance():
    # Call algorithm to sort packages for first truck
    second_truck_list()
    total_distance_2 = 0

    # Calculate total distance of the first truck and distance of each package -> O(n)
    for index in range(len(second_truck_index())):
        try:
            total_distance_2 = distance.get_total_distance(int(second_truck_index()[index]), int(second_truck_index()[index + 1]), total_distance_2)
            deliver_package = distance.get_time(distance.get_distance(int(second_truck_index()[index]), int(second_truck_index()[index + 1])), second_leave_times)
            truck2.packages_loaded[index][10] = (str(deliver_package))
            hash.ChainingHashTable.update(truck2.packages_loaded[index][0], truck2.packages_loaded, deliver_package)
        except IndexError:
            pass

    return total_distance_2


def third_truck_route():
    for index, outer in enumerate(truck3.packages_loaded):
        for inner in distance.get_address():
            if outer[1] == inner[1]:
                third_truck_distances.append(outer[0])
                truck1.packages_loaded[index][1] = inner[0]

    # Call algorithm to sort packages for first truck
    return get_shortest_route(truck3.route, 3, 0)


def third_truck_index():
    return third_optimized_truck_index_list


def third_truck_list():
    return third_optimized_truck


def third_truck_distance():
    # Call algorithm to sort packages for first truck
    third_truck_list()
    total_distance_3 = 0

    # Calculate total distance of the first truck and distance of each package -> O(n)
    for index in range(len(third_truck_index())):
        try:
            total_distance_3 = distance.get_total_distance(int(third_truck_index()[index]), int(third_truck_index()[index + 1]), total_distance_3)
            deliver_package = distance.get_time(distance.get_distance(int(third_truck_index()[index]), int(third_truck_index()[index + 1])), third_leave_times)
            truck3.packages_loaded[index][10] = (str(deliver_package))
            hash.ChainingHashTable.update(truck3.packages_loaded[index][0], truck3.packages_loaded, deliver_package)
        except IndexError:
            pass

    return total_distance_3

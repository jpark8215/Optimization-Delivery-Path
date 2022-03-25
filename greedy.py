
# This file takes data from the distance csv file, creates vertices based on the name of the location,
# and graphs the data using undirected edges. Each edge has a weight that represents the miles between each vertex

import distance
import package
import truck




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

# def get_shortest_route(address_list, truck_number, current_location):
#     if not len(address_list):
#         return address_list
#
#     lowest_value = 10
#     new_location = 0
#
#     for location in address_list:
#         for new_location in location:
#             i = distance.get_address_number(location)
#             if distance.get_distance(current_location, int(i)) <= lowest_value:
#                 lowest_value = distance.get_distance(current_location, int(i))
#                 new_location = location
#             # i = distance.get_address_number(new_location)
#
#     for location in address_list:
#         i = distance.get_address_number(location)
#         if distance.get_distance(current_location, int(i)) == lowest_value:
#             if truck_number == 1:
#                 first_optimized_truck.append(location)
#                 first_optimized_truck_index_list.append(i)
#                 address_list.pop(address_list.index(location))
#                 current_location = new_location
#                 get_shortest_route(address_list, 1, current_location)
#             elif truck_number == 2:
#                 second_optimized_truck.append(i)
#                 second_optimized_truck_index_list.append(i)
#                 address_list.pop(address_list.index(location))
#                 current_location = new_location
#                 get_shortest_route(address_list, 2, current_location)
#             elif truck_number == 3:
#                 third_optimized_truck.append(i)
#                 third_optimized_truck_index_list.append(i)
#                 address_list.pop(address_list.index(location))
#                 current_location = new_location
#                 get_shortest_route(address_list, 3, current_location)
#

first_optimized_truck = []
first_optimized_truck_index_list = []

second_optimized_truck = []
second_optimized_truck_index_list = []

third_optimized_truck = []
third_optimized_truck_index_list = []


def get_shortest_route(package_list, truck_number, current_location):
    if not len(package_list):
        return package_list

    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    shortest_dist = float()
    closest = truck.truck1.packages_loaded.pop()
    index = 0

    for index, outer in enumerate(truck.truck1.route):
        for inner in distance.get_address():
            if outer == inner[1]:
                dist = distance.get_distance(current_location, int(inner[0]))
                if dist < shortest_dist:
                    # first_optimized_truck.append(inner[1])
                    # first_optimized_truck_index_list.append(inner[0])
                    package_list.pop(package_list.index(inner[1]))
                    shortest_dist = dist
    index += 1

    return closest


first_optimized_truck.append(get_shortest_route(truck.truck1.packages_loaded, 1, 0))


# Insert 0 for the first index of each index list
first_optimized_truck_index_list.insert(0, '0')


# The following are all helper functions to return a desired value -> O(1)
def first_truck_index():
    return first_optimized_truck_index_list


def first_truck_list():
    return first_optimized_truck
print("list: ", first_truck_list())
#
#
# second_optimized_truck_index_list.insert(0, '0')
#
#
# def second_truck_index():
#     return second_optimized_truck_index_list
#
#
# def second_truck_list():
#     return second_optimized_truck
#
#
# third_optimized_truck_index_list.insert(0, '0')
#
#
# def third_truck_index():
#     return third_optimized_truck_index_list
#
#
# def third_truck_list():
#     return third_optimized_truck


# Empty lists created
first_delivery = []
second_delivery = []
third_delivery = []

first_truck_distances = []
second_truck_distances = []
third_truck_distances = []

# Times the trucks leave the hub
first_leave_times = ['8:00:00']
second_leave_times = ['9:10:00']
third_leave_times = ['11:00:00']

# # Set delivery_start to first_leave_time for all truck one packages -> O(n)
# for index, value in enumerate(csv_reader.get_first_delivery()):
#     csv_reader.get_first_delivery()[index][9] = first_leave_times[0]
#     first_delivery.append(csv_reader.get_first_delivery()[index])

# # Compare truck one addresses to address list -> O(n^2)
# for index, outer in enumerate(first_delivery):
#     for inner in distance.get_address():
#         if outer[2] == inner[2]:
#             first_truck_distances.append(outer[0])
#             first_delivery[index][1] = inner[0]


# total_distance_1 = 0
#
# # Calculate total distance of the first truck and distance of each package -> O(n)
#
# for index in range(len(first_optimized_truck_index_list)):
#     try:
#         total_distance_1 = distance.get_total_distance(int(first_optimized_truck_index_list[index]), int(first_optimized_truck_index_list[index + 1]), total_distance_1)
#
#         deliver_package = distance.get_time(distance.get_distance(int(first_optimized_truck_index_list[index]), int(first_optimized_truck_index_list[index + 1])), first_leave_times)
#         # first_truck_list()[index][10] = (datetime(deliver_package))
#         hash.ChainingHashTable.update(first_truck_list()[index][0], first_truck_index(), first_truck_list())
#     except IndexError:
#         pass
#
#
# def total_distance():
#     return total_distance_1

# # Make Predictions with k-nearest neighbors on the Iris Flowers Dataset
# from csv import reader
# from math import sqrt
#
#
# # Load a CSV file
# def load_csv(filename):
#     dataset = list()
#     with open(filename, 'r') as file:
#         csv_reader = reader(file)
#         for row in csv_reader:
#             if not row:
#                 continue
#             dataset.append(row)
#     return dataset
#
#
# # Convert string column to float
# def str_column_to_float(dataset, column):
#     for row in dataset:
#         row[column] = float(row[column].strip())
#
#
# # Convert string column to integer
# def str_column_to_int(dataset, column):
#     class_values = [row[column] for row in dataset]
#     unique = set(class_values)
#     lookup = dict()
#     for i, value in enumerate(unique):
#         lookup[value] = i
#         print('[%s] => %d' % (value, i))
#     for row in dataset:
#         row[column] = lookup[row[column]]
#     return lookup
#
#
# # Find the min and max values for each column
# def dataset_minmax(dataset):
#     minmax = list()
#     for i in range(len(dataset[0])):
#         col_values = [row[i] for row in dataset]
#         value_min = min(col_values)
#         value_max = max(col_values)
#         minmax.append([value_min, value_max])
#     return minmax
#
#
# # Rescale dataset columns to the range 0-1
# def normalize_dataset(dataset, minmax):
#     for row in dataset:
#         for i in range(len(row)):
#             row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])
#
#
# # Calculate the Euclidean distance between two vectors
# def euclidean_distance(row1, row2):
#     distance = 0.0
#     for i in range(len(row1) - 1):
#         distance += (row1[i] - row2[i]) ** 2
#     return sqrt(distance)
#
#
# # Locate the most similar neighbors
# def get_neighbors(train, test_row, num_neighbors):
#     distances = list()
#     for train_row in train:
#         dist = euclidean_distance(test_row, train_row)
#         distances.append((train_row, dist))
#     distances.sort(key=lambda tup: tup[1])
#     neighbors = list()
#     for i in range(num_neighbors):
#         neighbors.append(distances[i][0])
#     return neighbors
#
#
# # Make a prediction with neighbors
# def predict_classification(train, test_row, num_neighbors):
#     neighbors = get_neighbors(train, test_row, num_neighbors)
#     output_values = [row[-1] for row in neighbors]
#     prediction = max(set(output_values), key=output_values.count)
#     return prediction
#
#
# # Make a prediction with KNN on Iris Dataset
# filename = 'distance2.csv'
# dataset = load_csv(filename)
# for i in range(len(dataset[0]) - 1):
#     str_column_to_float(dataset, i)
# # convert class column to integers
# str_column_to_int(dataset, len(dataset[0]) - 1)
# # define model parameter
# num_neighbors = 5
# # define a new record
# row = [5.7, 2.9, 4.2, 1.3]
# # predict the label
# label = predict_classification(dataset, row, num_neighbors)
# print('Data=%s, Predicted: %s' % (row, label))
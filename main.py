# Jieun Park 001216539
import sys

import distance
import hash
import nearest
import package
import truck

# print(package.get_package)

# print("All truck & package data after loading: ")
# print("Truck 1 has", len(truck.truck1.packages_loaded), "packages")
# print("Truck 1 packages:", *truck.truck1.packages_loaded, sep="\n")
# print("Truck 2 has", len(truck.truck2.packages_loaded), "packages")
# print("Truck 2 packages:", *truck.truck2.packages_loaded, sep="\n")
# print("Truck 3 has", len(truck.truck3.packages_loaded), "packages")
# print("Truck 3 packages:", *truck.truck3.packages_loaded, sep="\n")

# print("Truck index:", nearest.first_optimized_truck_index_list)
# print("Truck index:", nearest.second_optimized_truck_index_list)
# print("Truck index:", nearest.third_optimized_truck_index_list)
# #
# print("Truck list:", nearest.first_optimized_truck_address)
# print("Truck list:", nearest.second_optimized_truck_address)
# print("Truck list:", nearest.third_optimized_truck_address)

# print(*nearest.first_optimized_packages_list, sep="\n")
# print(len(nearest.first_optimized_packages_list))
# print(*nearest.second_optimized_packages_list, sep="\n")
# print(len(nearest.second_optimized_packages_list))
# print(*nearest.third_optimized_packages_list, sep="\n")
# print(len(nearest.third_optimized_packages_list))

print("Total distance:", nearest.get_overall_distance())


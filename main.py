# Jieun Park 001216539

import distance
import package
import truck

print(package.get_package())

print(truck.truck1.packages_loaded)
print(truck.truck2.packages_loaded)
print(truck.truck3.packages_loaded)

print(len(truck.truck1.packages_loaded))
print(len(truck.truck2.packages_loaded))
print(len(truck.truck3.packages_loaded))

print(distance.get_all_distance_csv_data())
print(distance.get_all_address_csv_data())


# # Results
# print("All truck & package data after loading: ")
# print("Truck 1 has", len(truck.truck1.packages_loaded), "packages")
# print("Truck 1 packages:", *truck.truck1.packages_loaded, sep="\n")
# print("Truck 2 has", len(truck.truck2.packages_loaded), "packages")
# print("Truck 2 packages:", *truck.truck2.packages_loaded, sep="\n")
# print("Truck 3 has", len(truck.truck3.packages_loaded), "packages")
# print("Truck 3 packages:", *truck.truck3.packages_loaded, sep="\n")

print(truck.truck1.route)
print(truck.truck2.route)
print(truck.truck3.route)

# print(truck.first_truck_index())
# print(truck.first_truck_list())

print("Truck route:", truck.first_truck_route())
print("Truck route:", truck.second_truck_route())
print("Truck route:", truck.third_truck_route())

print("Truck index:", truck.first_truck_index())
print("Truck index:", truck.second_truck_index())
print("Truck index:", truck.third_truck_index())


print("Truck list:", truck.first_truck_list())
print("Truck list:", truck.second_truck_list())
print("Truck list:", truck.third_truck_list())

print("Truck distance:", truck.first_truck_distance())
print("Truck distance:", truck.second_truck_distance())
print("Truck distance:", truck.third_truck_distance())





# print("Truck route:", truck.first_truck_list())


class Main:
    # This is the display message that is shown when the user runs the program. The interface is accessible from here
    print('------------------------------')
    print('WGUPS Routing Program!')
    print('------------------------------\n')
#     print(f'Route was completed in {total_distance():.2f} miles.\n')
#
#     user_input = input("""
# Please select an option below to begin or type 'quit' to quit:
#     1. Get info for all packages at a particular time
#     2. Get info for a single package at a particular time
# """)
#
#     while user_input is not 'quit':
#         # Case if user selects Option #1
#         # Get info for all packages at a particular time -> O(n)
#         if user_input == '1':
#             try:
#                 input_time = input('Enter a time (HH:MM:SS): ')
#                 (hrs, mins, secs) = input_time.split(':')
#                 convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
#
#                 # Complexity ->  O(n^2)
#                 for count in range(1, 41):
#                     try:
#                         first_time = get_hash_map().get_value(str(count))[9]
#                         second_time = get_hash_map().get_value(str(count))[10]
#                         (hrs, mins, secs) = first_time.split(':')
#                         convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
#                         (hrs, mins, secs) = second_time.split(':')
#                         convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
#                     except ValueError:
#                         pass
#
#                     # Determine which packages have left the hub
#                     if convert_first_time >= convert_user_time:
#                         get_hash_map().get_value(str(count))[10] = 'At Hub'
#                         get_hash_map().get_value(str(count))[9] = 'Leaves at ' + first_time
#
#                         # Print package's current info
#                         print(
#                             f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
#                             f'Delivery status: {get_hash_map().get_value(str(count))[10]}'
#                         )
#
#                     # Determine which packages have left but have not been delivered
#                     elif convert_first_time <= convert_user_time:
#                         if convert_user_time < convert_second_time:
#                             get_hash_map().get_value(str(count))[10] = 'In transit'
#                             get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time
#
#                             # Print package's current info
#                             print(
#                                 f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
#                                 f'Delivery status: {get_hash_map().get_value(str(count))[10]}'
#                             )
#
#                         # Determine which packages have already been delivered
#                         else:
#                             get_hash_map().get_value(str(count))[10] = 'Delivered at ' + second_time
#                             get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time
#
#                             # Print package's current info
#                             print(
#                                 f'Package ID: {get_hash_map().get_value(str(count))[0]}, '
#                                 f'Delivery status: {get_hash_map().get_value(str(count))[10]}'
#                             )
#             except IndexError:
#                 print(IndexError)
#                 exit()
#             except ValueError:
#                 print('Invalid entry!')
#                 exit()
#
#         # Case if user selects Option #2
#         # Get info for a single package at a particular time -> O(n)
#         elif user_input == '2':
#             try:
#                 count = input('Enter a valid package ID: ')
#                 first_time = get_hash_map().get_value(str(count))[9]
#                 second_time = get_hash_map().get_value(str(count))[10]
#                 input_time = input('Enter a time (HH:MM:SS): ')
#                 (hrs, mins, secs) = input_time.split(':')
#                 convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
#                 (hrs, mins, secs) = first_time.split(':')
#                 convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
#                 (hrs, mins, secs) = second_time.split(':')
#                 convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
#
#                 # Determine which packages have left the hub
#                 if convert_first_time >= convert_user_time:
#
#                     get_hash_map().get_value(str(count))[10] = 'At Hub'
#                     get_hash_map().get_value(str(count))[9] = 'Leaves at ' + first_time
#
#                     # Print package's current info
#                     print(
#                         f'Package ID: {get_hash_map().get_value(str(count))[0]}\n'
#                         f'Street address: {get_hash_map().get_value(str(count))[2]}\n'
#                         f'Required delivery time: {get_hash_map().get_value(str(count))[6]}\n'
#                         f'Package weight: {get_hash_map().get_value(str(count))[7]}\n'
#                         f'Truck status: {get_hash_map().get_value(str(count))[9]}\n'
#                         f'Delivery status: {get_hash_map().get_value(str(count))[10]}\n'
#                     )
#
#                 # Determine which packages have left but have not been delivered
#                 elif convert_first_time <= convert_user_time:
#                     if convert_user_time < convert_second_time:
#                         get_hash_map().get_value(str(count))[10] = 'In transit'
#                         get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time
#
#                         # Print package's current info
#                         print(
#                             f'Package ID: {get_hash_map().get_value(str(count))[0]}\n'
#                             f'Street address: {get_hash_map().get_value(str(count))[2]}\n'
#                             f'Required delivery time: {get_hash_map().get_value(str(count))[6]}\n'
#                             f'Package weight: {get_hash_map().get_value(str(count))[7]}\n'
#                             f'Truck status: {get_hash_map().get_value(str(count))[9]}\n'
#                             f'Delivery status: {get_hash_map().get_value(str(count))[10]}\n'
#                         )
#
#                     # Determine which packages have already been delivered
#                     else:
#                         get_hash_map().get_value(str(count))[10] = 'Delivered at ' + second_time
#                         get_hash_map().get_value(str(count))[9] = 'Left at ' + first_time
#
#                         # Print package's current info
#                         print(
#                             f'Package ID: {get_hash_map().get_value(str(count))[0]}\n'
#                             f'Street address: {get_hash_map().get_value(str(count))[2]}\n'
#                             f'Required delivery time: {get_hash_map().get_value(str(count))[6]}\n'
#                             f'Package weight: {get_hash_map().get_value(str(count))[7]}\n'
#                             f'Truck status: {get_hash_map().get_value(str(count))[9]}\n'
#                             f'Delivery status: {get_hash_map().get_value(str(count))[10]}\n'
#                         )
#
#             except ValueError:
#                 print('Invalid entry')
#                 exit()
#
#         # Case 'exit'
#         # This exits the program
#         elif user_input == 'quit':
#             exit()
#
#         # Case Error
#         # Print Invalid Entry and quit the program
#         else:
#             print('Invalid entry!')
#             exit()
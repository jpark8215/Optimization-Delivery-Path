# Jieun Park 001216539
import distance
import greedy
import package
import truck

# print(package.get_package())

# print(truck.truck1.packages_loaded)
# print(truck.truck2.packages_loaded)
# print(truck.truck3.packages_loaded)
#
# print(len(truck.truck1.packages_loaded))
# print(len(truck.truck2.packages_loaded))
# print(len(truck.truck3.packages_loaded))
#
# print(distance.get_all_distance_csv_data())
# print(distance.get_all_address_csv_data())
#
# print("All truck & package data after loading: ")
# print("Truck 1 has", len(truck.truck1.packages_loaded), "packages")
# print("Truck 1 packages:", *truck.truck1.packages_loaded, sep="\n")
# print("Truck 2 has", len(truck.truck2.packages_loaded), "packages")
# print("Truck 2 packages:", *truck.truck2.packages_loaded, sep="\n")
# print("Truck 3 has", len(truck.truck3.packages_loaded), "packages")
# print("Truck 3 packages:", *truck.truck3.packages_loaded, sep="\n")


print("Truck index:", greedy.first_truck_index())
print("Truck index:", greedy.second_truck_index())
print("Truck index:", greedy.third_truck_index())

print("Truck list:", greedy.first_truck_list())
print("Truck list:", greedy.second_truck_list())
print("Truck list:", greedy.third_truck_list())

print(greedy.deliver_packages())
# print(greedy.get_distance())
# instructions = '''
# Please select an option from the list:
#     1. Get info on a specific package
#     2. Get info on all packages
#     3. Get one-liner info on all packages
#     4. Get info on truck travel distance
# '''
#
#
# def get_input(prompt: str) -> str:
#     """
#     Adds a prompt to the input and captures any EOF error and quits the app
#     """
#     try:
#         return input(f'{prompt}\n> ')
#     except EOFError:
#         sys.exit(0)
#
#
# def get_int_input(prompt: str) -> int:
#     """
#     Adds a prompt to the input and captures any EOF error and quits the app
#     """
#     while True:
#         try:
#             return int(get_input(prompt))
#         except ValueError:
#             print('Please enter an integer value')
#
#
# def print_package(package: Package, time: int) -> None:
#     print(f'Package ID: {package.id}')
#     print(f'Current status: {package.status(time)}')
#     print(f'Package due by: {package.formatted_deadline()}')
#     print(f'Package weight: {package.mass}')
#     print('Delivery address:')
#     print(package.street_address)
#     print(f'{package.city}, {package.state} {package.zipcode}')
#     print()
#
#
# def start_app(packages: HashMap[int, Package], trucks: list[Truck]) -> None:
#     """
#     Starts the command-line app for retrieving information between
#     """
#     print('Welcome to WGUPS Package Tracking.')
#     while True:
#         selection = get_input(instructions)
#
#         if selection == 'quit':
#             break
#
#         time = 0
#         if selection != '4':
#             while time == 0:
#                 try:
#                     string = get_input(
#                         'Please enter a time in the format of HH:MM')
#                     time = clock_to_minutes(string)
#                 except Exception:
#                     continue
#
#         if selection == '1':
#             while not (pkg_num := get_int_input('Please enter a valid package ID')) in packages:
#                 print(f'Package with ID "{pkg_num}" was not found')
#
#             print_package(packages.get(pkg_num), time)
#
#         elif selection == '2':
#             for (_, package) in packages:
#                 print_package(package, time)
#
#         elif selection == '3':
#             package_list = [package for (_, package) in packages]
#             package_list.sort(key=lambda p: p.id)
#             for package in package_list:
#                 print(package.info(time))
#
#         elif selection == '4':
#             for truck in trucks:
#                 print(
#                     f'Truck {truck.number} traveled {round(truck.miles_traveled, 1)} miles')
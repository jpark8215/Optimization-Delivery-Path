# The Truck Class assists in creating truck objects which will be loaded with packages
import distance


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


# def first_truck_route():
#     inner_index = []
#     for index, outer in enumerate(truck1.route):
#         for inner in distance.get_address():
#             if outer == inner[1]:
#                 inner_index.append(inner[0])
#                 # truck1.update_route(inner[0])
#     return inner_index






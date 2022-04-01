# The Truck Class assists in creating truck objects which will be loaded with packages
import distance


class Truck:

    # Constructor to initialize packages on the truck, route, delivery start time, and mileage
    def __init__(self):
        self.packages_loaded = []
        self.route = []
        self.start_time = None
        self.delivery_time = None
        self.end_time = None

    # Put package on truck
    def insert(self, p):
        self.packages_loaded.append(p)  # puts the package onto the truck
        self.route.append(p[1])  # package[1] == street address where the package is going

    # Delivered packages are removed from the truck
    def remove(self, p):
        self.packages_loaded.remove(p)  # takes the package off the truck
        self.route.remove(p[1])  # removes the address from the route

    # Leave the hub and start the delivery route
    def start_delivery(self, start):
        self.start_time = start

    def location_time(self, current):
        self.delivery_time = current

    def back_to_hub_time(self, end):
        self.end_time = end


# Create truck objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

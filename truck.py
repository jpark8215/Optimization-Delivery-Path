# Truck class constructor
# Assists in creating truck objects with packages
# Initializes packages on the truck, route, and delivery start time
class Truck:

    def __init__(self):
        self.packages_loaded = []
        self.route = []
        self.start_time = None

    # Adds package on truck
    def insert(self, p):
        self.packages_loaded.append(p)
        self.route.append(p[1])

    # Removes optimized packages from truck
    def remove(self, p):
        self.packages_loaded.remove(p)  # takes the package off the truck
        self.route.remove(p[1])  # removes the address from the route

    # Leaves hub and starts delivery
    def start_delivery(self, start):
        self.start_time = start


# Creates truck objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

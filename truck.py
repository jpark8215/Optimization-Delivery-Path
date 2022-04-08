"""
DEFINE CLASS Truck:

    DEFINE FUNCTION __init__(self):
        SET self.packages_loaded TO []
        SET self.route TO []
        SET self.start_time TO None

    DEFINE FUNCTION insert(self, p):
        self.packages_loaded.append(p)
        self.route.append(p[1])

    DEFINE FUNCTION remove(self, p):
        self.packages_loaded.remove(p)  # takes the package off the truck
        self.route.remove(p[1])  # removes the address from the route

    DEFINE FUNCTION start_delivery(self, start):
        SET self.start_time TO start


SET truck1 TO Truck()
SET truck2 TO Truck()
SET truck3 TO Truck()
"""


# Truck class constructor
# Assists in creating truck objects with packages
# Initializes packages on the truck, route, and delivery start time
class Truck:

    # O(1)
    def __init__(self):
        self.packages_loaded = []
        self.route = []
        self.start_time = None

    # O(1)
    # Adds package on truck
    def insert(self, p):
        self.packages_loaded.append(p)
        self.route.append(p[1])

    # O(1)
    # Removes optimized packages from truck
    def remove(self, p):
        self.packages_loaded.remove(p)  # takes the package off the truck
        self.route.remove(p[1])  # removes the address from the route

    # O(1)
    # Leaves hub and starts delivery
    def start_delivery(self, start):
        self.start_time = start


# Creates truck objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

import csv
import truck
from hash import ChainingHashTable


# Package class constructor
# Initializes packages
class Package:

    def __init__(self, id, address, city, state, zip, deadline, weight, note, start, time_at_location, delivered_time, status):
        self.ID = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.start = start
        self.location = time_at_location
        self.delivered = delivered_time
        self.status = status

    # Overwrites print(Package) otherwise prints object reference
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.note, self.start,
            self.location, self.delivered, self.status)


# O(N)
# Gets package data from csv file and assigns data meaningful names
def load_package_data(filename):
    with open(filename) as package_file:
        package_data = csv.reader(package_file, delimiter=',')
        next(package_data)
        for p in package_data:
            p_id = int(p[0])
            p_address = p[1]
            p_city = p[2]
            p_state = p[3]
            p_zip = p[4]
            p_deadline = p[5]
            p_weight = p[6]
            p_note = p[7]
            p_start = p[8]
            p_location = p[9]
            p_delivered = p[10]
            p_status = ''

            # Loads truck with constrains
            if p_deadline == '9:00 AM':
                truck.truck1.insert(p)

            if p_deadline == '10:30 AM' and p_note != 'Delayed on flight':
                truck.truck1.insert(p)

            if p_deadline == 'EOD' and p_zip == '84104' and p_address == '2010 W 500 S':
                truck.truck1.insert(p)

            if p_deadline == '10:30 AM' and p_note == 'Delayed on flight':
                truck.truck2.insert(p)

            if p_deadline == 'EOD' and p_note == 'Can only be on truck 2':
                truck.truck2.insert(p)

            if p_deadline == 'EOD' and p_zip == '84119' and p_note != 'Can only be on truck 2':
                truck.truck3.insert(p)

            if p_deadline == 'EOD' and p_note == 'Wrong address listed':
                p[1] = '410 S State St'
                p[4] = '84111'
                truck.truck2.insert(p)

            if p_deadline == 'EOD' and p_zip == '84106':
                truck.truck3.insert(p)

            if p_deadline == 'EOD' and p_zip == '84115':
                truck.truck3.insert(p)

            # Checks packages that are not loaded and adds to trucks
            if p not in truck.truck1.packages_loaded and p not in truck.truck2.packages_loaded and p not in truck.truck3.packages_loaded:
                if len(truck.truck2.packages_loaded) < 12:
                    truck.truck2.insert(p)
                elif len(truck.truck3.packages_loaded) < 15:
                    truck.truck3.insert(p)
                else:
                    print("package could not be loaded", p_id)

            # p object p = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight, p_note, p_start,
            # p_location, p_delivered)

            # insert packages into the hash table
            package_hash.insert(p_id, p)


# Hash table instance
package_hash = ChainingHashTable()

# Loads packages to hash Table
load_package_data('package.csv')


# O(N)
# Gets data from hash table
def get_package():
    for i in range(len(package_hash.table) + 30):
        print("Package: {}".format(package_hash.search(i + 1)))


# O(1)
# Searches data with id from hash table and returns selected data
def search_package(id):
    package = package_hash.search(id)
    number = package[0]
    address = package[1]
    deadline = package[5]
    city = package[2]
    zipcode = package[4]
    weight = package[6]
    status = package[11]
    result = " Package #: " + number + "\n " + "Address: " + address + "\n " + "Deadline: " + deadline + "\n " \
             + "City: " + city + "\n " + "Zipcode: " + zipcode + "\n " + "Weight: " + weight + "\n " + "Status: " \
             + status + "\n "
    print(result)


# def search_package_address(address):
#     i = 0
#     for i in package_hash.table:
#         print(i)
#         print(package_hash.table)
#         if package_hash.search(i)[1] == address:
#             print(package_hash.search(i)[1])
#
#
#             package = package_hash.search(i)
#             number = package[0]
#             address = package[1]
#             deadline = package[5]
#             city = package[2]
#             zipcode = package[4]
#             weight = package[6]
#             status = package[11]
#             result = " Package #: " + number + "\n " + "Address: " + address + "\n " + "Deadline: " + deadline + "\n " \
#                  + "City: " + city + "\n " + "Zipcode: " + zipcode + "\n " + "Weight: " + weight + "\n " + "Status: " \
#                  + status + "\n "
#             i += 1
#
#             print(result)


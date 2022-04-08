import csv
import truck
from hash import ChainingHashTable

'''
DEFINE CLASS Package:

    DEFINE FUNCTION __init__(self, id, address, city, state, zip, deadline, weight, note, start, time_at_location, delivered_time, status):
        SET self.ID TO id
        SET self.address TO address
        SET self.city TO city
        SET self.state TO state
        SET self.zip TO zip
        SET self.deadline TO deadline
        SET self.weight TO weight
        SET self.note TO note
        SET self.start TO start
        SET self.location TO time_at_location
        SET self.delivered TO delivered_time
        SET self.status TO status


    DEFINE FUNCTION __str__(self):
        RETURN "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.note, self.start,
            self.location, self.delivered, self.status)


DEFINE FUNCTION load_package_data(filename):
    with open(filename) as package_file:
        SET package_data TO csv.reader(package_file, delimiter=',')
        next(package_data)
        FOR p IN package_data:
            SET p_id TO int(p[0])
            SET p_address TO p[1]
            SET p_city TO p[2]
            SET p_state TO p[3]
            SET p_zip TO p[4]
            SET p_deadline TO p[5]
            SET p_weight TO p[6]
            SET p_note TO p[7]
            SET p_start TO p[8]
            SET p_location TO p[9]
            SET p_delivered TO p[10]
            SET p_status TO ''

            IF p_deadline EQUALS '9:00 AM':
                truck.truck1.insert(p)

            IF p_deadline EQUALS '10:30 AM' and p_note != 'Delayed on flight':
                truck.truck1.insert(p)

            IF p_deadline EQUALS 'EOD' and p_zip EQUALS '84104' and p_address EQUALS '2010 W 500 S':
                truck.truck1.insert(p)

            IF p_deadline EQUALS '10:30 AM' and p_note EQUALS 'Delayed on flight':
                truck.truck2.insert(p)

            IF p_deadline EQUALS 'EOD' and p_note EQUALS 'Can only be on truck 2':
                truck.truck2.insert(p)

            IF p_deadline EQUALS 'EOD' and p_zip EQUALS '84119' and p_note != 'Can only be on truck 2':
                truck.truck3.insert(p)

            IF p_deadline EQUALS 'EOD' and p_note EQUALS 'Wrong address listed':
                SET p[1] TO '410 S State St'
                SET p[4] TO '84111'
                truck.truck2.insert(p)

            IF p_deadline EQUALS 'EOD' and p_zip EQUALS '84106':
                truck.truck3.insert(p)

            IF p_deadline EQUALS 'EOD' and p_zip EQUALS '84115':
                truck.truck3.insert(p)

            IF p not IN truck.truck1.packages_loaded and p not IN truck.truck2.packages_loaded and p not IN truck.truck3.packages_loaded:
                IF len(truck.truck2.packages_loaded) < 12:
                    truck.truck2.insert(p)

                ELSEIF len(truck.truck3.packages_loaded) < 15:
                    truck.truck3.insert(p)

                ELSE:
                    OUTPUT("package could not be loaded", p_id)

            SET # p object p TO Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight, p_note, p_start,
            # p_location, p_delivered)

            package_hash.insert(p_id, p)


SET package_hash TO ChainingHashTable()

load_package_data('package.csv')


DEFINE FUNCTION get_package():
    FOR i IN range(len(package_hash.table) + 30):
        OUTPUT("Package: {}".format(package_hash.search(i + 1)))


DEFINE FUNCTION search_package(id):
    SET package TO package_hash.search(id)
    SET number TO package[0]
    SET address TO package[1]
    SET deadline TO package[5]
    SET city TO package[2]
    SET zipcode TO package[4]
    SET weight TO package[6]
    SET status TO package[11]
    SET result TO " Package #: " + number + "\n " + "Address: " + address + "\n " + "Deadline: " + deadline + "\n " \
             + "City: " + city + "\n " + "Zipcode: " + zipcode + "\n " + "Weight: " + weight + "\n " + "Status: " \
             + status + "\n "
    OUTPUT(result)
'''


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

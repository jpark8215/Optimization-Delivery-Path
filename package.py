import csv
import truck
from hash import ChainingHashTable


# Package class constructor
class Package:

    def __init__(self, ID, address, city, state, zip, deadline, weight, note, start, location, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.start = start
        self.location = location
        self.status = status

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.note, self.start, self.location, self.status )


def load_package_data(filename):
    with open(filename) as package_file:
        package_data = csv.reader(package_file, delimiter=',')
        next(package_data)  # skip header
        for p in package_data:
            pID = int(p[0])
            pAddress = p[1]
            pCity = p[2]
            pState = p[3]
            pZip = p[4]
            pDeadline = p[5]
            pWeight = p[6]
            pNote = p[7]
            pStart = p[8]
            pLocation = p[9]
            pStatus = p[10]

            if pDeadline == '9:00 AM' and pNote == '':
                truck.truck1.insert(p)

            if pDeadline == '10:30 AM' and pNote == 'Must be delivered with':
                truck.truck1.insert(p)

            if pDeadline == '10:30 AM' and pNote == '':
                truck.truck1.insert(p)

            # Second truck's delivery
            if pDeadline == '10:30 AM' and pNote == 'Delayed on flight':
                truck.truck2.insert(p)

            # First truck's first delivery
            if pDeadline == 'EOD' and pNote == 'Can only be on truck 2':
                truck.truck2.insert(p)

            if pDeadline == 'EOD' and pNote == 'Delayed on flight':
                truck.truck3.insert(p)

            # Correct incorrect package details
            if pDeadline == 'EOD' and pNote == 'Wrong address listed':
                truck.truck3.insert(p)

            if pDeadline == 'EOD' and pNote == '':
                # if len(truck.truck1.packages_loaded) < 5:
                #     truck.truck1.insert(p)
                if len(truck.truck2.packages_loaded) < 12:
                    truck.truck2.insert(p)
                elif len(truck.truck3.packages_loaded) < 15:
                    truck.truck3.insert(p)
                else:
                    print("package could not be loaded", pID)

            # p object
            p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pNote, pStart, pLocation, pStatus)

            # insert it into the hash table
            package_hash.insert(pID, p)


# Hash table instance
package_hash = ChainingHashTable()

# Load packages to Hash Table
load_package_data('package.csv')


def get_package():
    print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(package_hash.table) + 1):
        print("Package: {}".format(package_hash.search(i + 1)))  # 1 to 11 is sent to myHash.search()


def search_package(ID):
    result = package_hash.search(ID)
    print(result)

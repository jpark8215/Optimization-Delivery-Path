import csv
from hash import ChainingHashTable


# Package class constructor
class Package:
    def __init__(self, ID, address, city, state, zip, deadline, mass, note):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.note = note

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.mass, self.note)


def load_package_data():
    with open('package.csv') as package_file:
        package_data = csv.reader(package_file, delimiter=',')
        next(package_data)  # skip header
        for row in package_data:
            pID = int(row[0])
            pAddress = row[1]
            pCity = row[2]
            pState = row[3]
            pZip = row[4]
            pDeadline = row[5]
            pMass = row[6]
            pNote = row[7]

            # row object
            p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pMass, pNote)

            # insert it into the hash table
            package_hash.insert(pID, p)


# Hash table instance
package_hash = ChainingHashTable()

# Load packages to Hash Table
load_package_data()


def get_package_data():
    print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(package_hash.table) + 1):
        print("Package: {}".format(package_hash.search(i + 1)))  # 1 to 11 is sent to myHash.search()



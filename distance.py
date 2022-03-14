import csv


# distance_list = list(csv.reader(open('distance.csv'), delimiter=','))


# This function grabs the address csv file.
# O(N)
def get_address_data():
    address_data = []
    with open('address.csv') as address_file:
        csv_reader = csv.reader(address_file, delimiter=',')
        for row in csv_reader:
            address_data.append(row)
    return address_data


# This function grabs the entire distance csv file.
# O(N)
def get_distance_data():
    distance_data = []
    with open('distance.csv') as distance_file:
        csv_reader = csv.reader(distance_file, delimiter=',')
        # next(csv_reader, None)
        for row in csv_reader:
            distance_data.append(row)
    return distance_data


# Read CSV files
with open('distance.csv') as csvfile:
    distance_csv = list(csv.reader(csvfile, delimiter=','))

    # Calculate the total distance from row/column values -> O(1)
    def get_distance(row, col):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return float(distance)
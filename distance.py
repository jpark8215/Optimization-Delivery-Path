import csv

# Read CSV files
import datetime

with open('distance2.csv') as distance_file:
    distance_csv = list(csv.reader(distance_file, delimiter=','))

    # Calculate the total distance from row/column values -> O(1)
    def get_distance(row, col):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[row][col]
        return float(distance)

    # Calculate the total distance from row/column values -> O(1)
    def get_total_distance(row, col, total):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]
        return total + float(distance)

# This function grabs the entire distance csv file.
# This is needed in order to create edges between vertex_a and vertex_b
# O(N)
    def get_all_distance_csv_data():
        all_distance_cvs = []
        # with open(filename) as all_distance_file:
        # distance_csv_reader = csv.reader(distance_file)
        for row in distance_csv:
            all_distance_cvs.append(row)
        return all_distance_cvs

    # Calculate total distance for a given truck -> O(n)
    def get_time(distance, truck_list):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        truck_list.append(final_time)
        total = datetime.timedelta()
        for i in truck_list:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        return total


with open('address.csv') as address_file:
    address_csv = list(csv.reader(address_file, delimiter=','))

    # This function grabs the address csv file.
    # O(N)
    def get_address():
        address = address_csv
        return address

# This function grabs the entire distance csv file.
# This is needed in order to create edges between vertex_a and vertex_b
# O(N)
    def get_all_address_csv_data():
        all_address_cvs = []
        # with open(filename) as all_address_file:
        # address_csv_reader = csv.reader(address_file)
        # next(address_csv_reader, None)
        for row in address_csv:
            all_address_cvs.append(row)
        return all_address_cvs

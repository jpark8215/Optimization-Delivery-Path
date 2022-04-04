import csv

with open('distance2.csv') as distance_file:
    distance_csv = list(csv.reader(distance_file, delimiter=','))

    # O(1)
    # Calculates distance from row/column values
    def get_distance(row, col):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[row][col]

        return float(distance)

    # O(1)
    # Calculates total distance from row/column values
    def get_total_distance(row, col, total):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return total + float(distance)

    # O(N)
    # Gets entire distance from csv file
    def get_all_distance_csv_data():
        all_distance_cvs = []
        for row in distance_csv:
            all_distance_cvs.append(row)

        return all_distance_cvs

    # O(N)
    # Converts start time into base time
    # Adds base time to time calculated by dividing total distance from nearest.py by speed
    def get_time(distance, optimized_packages_list):
        base_time = 0.0

        for i in range(len(optimized_packages_list)):
            (h, m, s) = optimized_packages_list[i][8].split(':')
            base_time = (int(s)/3600) + (int(m)/60) + int(h)

        time = distance / 18 + float(base_time)
        hours = int(time)
        minutes = ((time * 60) % 60)
        seconds = ((time * 3600) % 60)
        final_time = "%d:%02d:%02d" % (hours, minutes, seconds)

        return final_time


with open('address.csv') as address_file:
    address_csv = list(csv.reader(address_file, delimiter=','))

    # O(N)
    # Gets address id and address from csv file
    def get_address():
        address = []
        for row in address_csv:
            address_data = [row[0], row[2]]
            address.append(address_data)
        return address

    # O(N)
    # Gets all address data from csv file
    def get_all_address_csv_data():
        all_address_cvs = []
        for row in address_csv:
            all_address_cvs.append(row)
        return all_address_cvs

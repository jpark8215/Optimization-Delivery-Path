import csv

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
        for row in distance_csv:
            all_distance_cvs.append(row)

        return all_distance_cvs

    # Calculate total distance for a given truck -> O(n)
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

    # This function grabs the address csv file.
    # O(N)
    def get_address():
        address = []
        for row in address_csv:
            # parse into a dictionary for easy data access later
            address_data = [row[0], row[2]]
            # append to list
            address.append(address_data)
        return address

# This function grabs the entire distance csv file.
# This is needed in order to create edges between vertex_a and vertex_b
# O(N)
    def get_all_address_csv_data():
        all_address_cvs = []
        for row in address_csv:
            all_address_cvs.append(row)
        return all_address_cvs

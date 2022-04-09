import csv
'''
 with open('distance2.csv') as distance_file:
    SET distance_csv TO list(csv.reader(distance_file, delimiter=','))

    DEFINE FUNCTION get_distance(row, col):
        SET distance TO distance_csv[row][col]
        IF distance EQUALS '':
            SET distance TO distance_csv[row][col]
        RETURN float(distance)

    DEFINE FUNCTION get_total_distance(row, col, total):
        SET distance TO distance_csv[row][col]
        IF distance EQUALS '':
            SET distance TO distance_csv[col][row]
        RETURN total + float(distance)

    DEFINE FUNCTION get_all_distance_csv_data():
        SET all_distance_cvs TO []
        FOR row IN distance_csv:
            all_distance_cvs.append(row)
        RETURN all_distance_cvs


    DEFINE FUNCTION get_time(distance, optimized_packages_list):
        SET base_time TO 0.0

        FOR i IN range(len(optimized_packages_list)):
            SET (h, m, s) TO optimized_packages_list[i][8].split(':')
            SET base_time TO (int(s) / 3600) + (int(m) / 60) + int(h)

        SET time TO distance / 18 + float(base_time)
        SET hours TO int(time)
        SET minutes TO ((time * 60) % 60)
        SET seconds TO ((time * 3600) % 60)
        SET final_time TO "%d:%02d:%02d" % (hours, minutes, seconds)
        
        RETURN final_time


with open('address.csv') as address_file:
    SET address_csv TO list(csv.reader(address_file, delimiter=','))

    DEFINE FUNCTION get_address():
        SET address TO []
        FOR row IN address_csv:
            SET address_data TO [row[0], row[2]]
            address.append(address_data)
        RETURN address

    DEFINE FUNCTION get_all_address_csv_data():
        SET all_address_cvs TO []
        FOR row IN address_csv:
            all_address_cvs.append(row)
        RETURN all_address_cvs 
'''
# Gets data from file and stores in list
with open('distance2.csv') as distance_file:
    distance_csv = list(csv.reader(distance_file, delimiter=','))

    # O(1)
    # Gets distance from row/column values
    def get_distance(row, col):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[row][col]

        return float(distance)

    # O(1)
    # Gets distance from row/column values and adds the value to previously obtained sum
    def get_total_distance(row, col, total):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return total + float(distance)

    # O(N)
    # Gets entire distance data from csv file and stores in list
    def get_all_distance_csv_data():
        all_distance_cvs = []
        for row in distance_csv:
            all_distance_cvs.append(row)

        return all_distance_cvs

    # O(N)
    # Converts start time in index 8 of optimized list from greedy.py into base time
    # Adds base time and time calculated by dividing total distance from greedy.py by speed
    # Returns delivered time of package
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

# Gets data from file and stores in list
with open('address.csv') as address_file:
    address_csv = list(csv.reader(address_file, delimiter=','))

    # O(N)
    # Gets address id and address from csv file and stores in list
    def get_address():
        address = []
        for row in address_csv:
            address_data = [row[0], row[2]]
            address.append(address_data)
        return address

    # O(N)
    # Gets all address data from csv file and stores in list
    def get_all_address_csv_data():
        all_address_cvs = []
        for row in address_csv:
            all_address_cvs.append(row)
        return all_address_cvs

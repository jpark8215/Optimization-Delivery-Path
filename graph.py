# import csv
#
# """
# GRAPH BIG O ANALYSIS
# NOTES:
# RESOURCE: https://wiki.python.org/moin/TimeComplexity
# Arithmetic: O(1)
# INITIALIZE AND SET = one operation = 1
# Multiplication:
# FOR = N operations if each element of data needs to be accessed
# FOR = LogN if it cuts down the amount of data that needs to be accessed (merge sort)
# WHILE = LogN because it potentially runs shorter than the length of all the data elements
# ------------------------------------------------------------------------------------------------------------------------
# BIG O       |                                           PSEUDOCODE                                                     |
# ------------------------------------------------------------------------------------------------------------------------
# >> Clean and sort distance data into a base matrix dist_tbl_graph which can be used to create the undirected
# >> adjacency matrix
# O(1)........INITIALIZE AND SET distance_table = DISTANCES CSV FILE
# O(1)........INITIALIZE AND SET TO EMPTY LISTS: dist_tbl_hash, distances, address_hash
#
#             * *************************************************************** *
#             * OPEN is just accessing a pointer in memory allowing access to   *
#             * the data file as variable 'dt'.                                 *
#             * This does not require any iterations therefore it has a run     *
#             * time of O(1).                                                   *
#             * *************************************************************** *
# O(1)........OPEN distance_table AS dt
#
#                  * *************************************************************** *
#                  * string.replace('current string', 'replacement string')          *
#                  * current_string = 1                                              *
#                  * replacement_string = 1                                          *
#                  * len(dt) = N                                                     *
#                  * len(dt.row) = N                                                 *
#                  * O(f(len(dt)) * f(len(dt.row)) + 2 = N * N + 2 = O(N^2)          *
#                  * *************************************************************** *
# O(N^2)...........INITIALIZE AND SET LIST filtered = REMOVE ALL '\n' FOR EACH STRING LINE IN dt
#                  * *************************************************************************************************** *
#                  * Return a reader object which will iterate over lines in the given csvfile. csvfile can be any object*
#                  * which supports the iterator protocol and returns a string each time its __next__() method is called *
#                  * To iterate over each line means it must include a for loop like this example:                       *
#                  *      for index in range(0, len(filtered), 1): add filtered row to reader[index]                     *
#                  * index = N                                                                                           *
#                  * len(filtered) = N                                                                                   *
#                  * O(f(index) * f(filtered)) = N * N = O(N^2)                                                          *
#                  * *************************************************************************************************** *
# O(N).............INITIALIZE AND SET LIST reader = csv.reader(filtered)
#
#             >>> counter for rows in reader
# O(1).............INITIALIZE AND SET INT row_id = 0
#
#                  ******************************************************** *
#                  * len(reader) = N + 1                                    *
#                  * ****************************************************** *
#              >>> append each row in reader to list dist_tbl_hash
# O(N + 1).........FOR EACH INDEX IN RANGE(0, len(reader), 1):
#                     >> base case
# O(2N + 1)...........IF row_id IS 0
#                         INITIALIZE AND SET INT address_id TO 0
#
#                         * ****************************************************** *
#                         * len(reader) = N                                        *
#                         * len(reader.row) = N                                    *
#                         * O(f(len(reader)) * f(len(reader.row) = O(N^2)          *
#                         * ****************************************************** *
#                     >>> add address_id (hash) to each row then append row data
# O((2N + 1)(N + 1))......FOR EACH <T> column IN row
#                         >>> column base case
# O((2N +1)(4N + 1))..........IF column IS NOT 0
#                                 SET LIST column = [address_id + 1, column]
#                                 SET LIST row INDEX address_id TO column
#                                 INCREMENT address_id BY 1
# O(N^2).................END FOR<<<<<
#                     END IF<<<<<
#
#                     >>>> continue first loop - O(N + 1)
#                     * ****************************************************** *
#                     * https://wiki.python.org/moin/TimeComplexity            *
#                     * EXTEND = O(K) (K=size of temp_list)                    *
#                     * APPEND = O(1)                                          *
#                     * len(temp_list) = K                                     *
#                     * len(row) = number of locations = N                     *
#                     * O(f(len(row)) * f(len(temp_list) = O(NK) = O(N)        *
#                     * ****************************************************** *
#                 >>> append previously formatted row to dist_tbl_hash
# O((1N +1)(NK))......INITIALIZE AND SET LIST temp_list = [row_id]
#                 >>> O(K)
#                     EXTEND LIST temp_list WITH LIST row
#                     APPEND LIST temp_list TO LIST dist_tbl_hash
#                     INCREMENT row_id BY 1
# O(KN^2).........END FOR<<<<<
#
#                 >>>>> new first level for loop
#                 * ****************************************************** *
#                 * len(dist_tbl_hash) = number of locations = N           *
#                 * O(f(len(dist_tbl_hash)) = O(N)                         *
#                 * ****************************************************** *
#             >>> clean and format dist_tbl_hash, build address_hash and distances_list
# O(5N)...........FOR EACH LIST row IN LIST dist_tbl_hash
#
#                     * ****************************************************** *
#                     * O(f(len(dist_tbl_hash) + 1) = O(N)                     *
#                     * ****************************************************** *
#                 >>> base case - top row of csv is a list of addresses - this row is deleted here
#                 >>> then create new row[0] with HUB data list
#                     IF row[0] IS 0
#                         DELETE row[0]
#                     >>> HUB address
#                         INITIALIZE AND SET STRING street_address = "4001 South 700 East"
#                     >>> new row[0] is the HUB data list
#                         SET STRING row[0][1] = STRING street_address
#                         APPEND LIST [0, street_address] TO LIST address_hash
#                     END IF
#                     >>>>> second level loop
#                     * ****************************************************** *
#                     * len(s) = length of string = N                          *
#                     * s.index(c) -> loop to index each character in s        *
#                     *                then loop back through to find c        *
#                     *                    return index of c                   *
#                     * i = length of string = N                               *
#                     * c = length of string = N                               *
#                     * O(f(len(s) * f(len(s)) * f(len(s)) = N^3               *
#                     * ****************************************************** *
#                     * NOTE: for built in function s.index(c)                 *
#                     * Since N = the length of the string street address,     *
#                     * N is expected to be less  than 50.                     *
#                     * Typically having O(N^3) would be less than ideal but   *
#                     * N is expected to be < 50 N^3 will not have a           *
#                     * significant impact on the run time here.               *
#                     *                                                        *
#                     * s.INDEX(c) iterates over the string until the          *
#                     * matching value is found.                               *
#                     * ****************************************************** *
#                     * Slicing a string like so s[start index : end index] is *
#                     * accomplished with the python built in feature, slice.  *
#                     * At https://wiki.python.org/moin/TimeComplexity it is   *
#                     * said that getting a slice costs O(K) time.             *
#                     * ****************************************************** *
#
#                 >>> clean and build the rest of the data for the lists build address_hash and distances_list
#                 >>> extract zipcode and street address
#                 >>> https://stackoverflow.com/questions/10059554/inserting-characters-at-the-start-and-end-of-a-string
#                 >>> loop through each character of string s and extract zipcode and street address
#
#                     INITIALIZE AND SET STRING s = FUNCTION STR(row[2])
# O(12N^3*2K).........FOR EACH character IN STRING s
#                         IF c IS "("
#                         >>> O(N^2) - see NOTE above setting i here saves time later when slicing the string
#                             SET INT i = s.INDEX(c)
#
#                             SET INT address_id = row[0]
#                         >>> account for zero based indexing
#                             DECREMENT address_id BY 1
#
#                         >>> get zipcode and string SLICE O(K) - see NOTE above
#                             SET STRING zipcode = s[i + 1:-1]
#                             SET STRING street _address = s[1:i]
#
#                         >>> build list address_hash
#                             SET STRING row[2] = STRING street_address
#                             APPEND LIST [address_id, street_address, zipcode] TO LIST address_hash
#
#                         BREAK
#                         END IF
#                     END FOR
#                 >>> build distances_graph
#                 >>> O(K)
#                     IF row[0] IS NOT A LIST
#                         INITIALIZE AND SET LIST temp_list = [row[0] - 1]
#                         INITIALIZE AND SET LIST all_miles_in_current_list = LIST row FROM INDEX 3 TO LAST INDEX
#                         EXTEND LIST temp_list WITH LIST all_miles_in_current_list
#                         APPEND LIST temp_list TO LIST distances
# O(KN^3)         END FOR
# ------------------------------------------------------------------------------------------------------------------------
# BIG O TOTAL
# ------------------------------------------------------------------------------------------------------------------------
# O(KN^3)
# """
# # import distance data
# distance_table = './distance2.csv'
#
# # initial hash for distances, excludes vertices (miles) for all locations at each node
# dist_tbl_hash = []
# # distance graph for algorithm, includes vertices (miles) for all locations at each node
# distances = []
# # address hash, list of lists, each sublist = [location_id, street_address, zipcode]
# address_hash = []
#
# """
# open the file and clean the unnecessary information, new lines, and spaces
# BIG O total: O(N^3)
# """
# with open(distance_table) as dt:
#     # remove new line \n
#     # O(N^2)
#     filtered = (line.replace('\n', '') for line in dt)
#
#     # O(N)
#     reader = csv.reader(filtered)
#     # row_id is hash for dist_tbl_hash
#     row_id = 0
#     # skip first row
#     # O(1)
#     dt.readline()
#     # append each row to dist_tbl_hash
#     for row in reader:
#         # hash each row with row_id and row
#         if row_id == 0:
#             address_id = 0
#             for col in row:
#                 if col != 0:
#                     col = [address_id + 1, col]
#                     row[address_id] = col
#                     address_id += 1
#
#         temp_list = [row_id]
#         # use built in extend method to iterate over row and add each element of the row
#         temp_list.extend(row)
#         dist_tbl_hash.append(temp_list)
#         row_id += 1
#
#     # clean dist_tbl_hash, build address_hash, distances_list
#     for row in dist_tbl_hash:
#         if row[0] == 0:
#             del row[0]
#             street_address = "4001 South 700 East"
#             row[0][1] = street_address
#             address_hash.append([0, street_address])
#         s = str(row[2])
#         for c in s:
#             if c == "(":
#                 # extract zipcode from the street address
#                 i = s.index(c)
#                 address_id = row[0]
#                 # subtract 1 for 0 based indexing
#                 address_id = address_id - 1
#                 zipcode = s[i + 1:-1]
#                 street_address = s[1:i]
#
#                 # build address_hash
#                 row[2] = street_address
#                 address_hash.append([address_id, street_address, zipcode])
#                 break
#
#         # build distances_graph
#         if isinstance(row[0], list) is False:
#             temp_list = [row[0] - 1]
#             all_miles_in_current_node = row[3::]
#             temp_list.extend(all_miles_in_current_node)
#             distances.append(temp_list)
#
# """
# FUNCTION build_adjacency_matrix
# The purpose of this block of code is to fill in the empty strings with the corresponding mileage from the matching
# node. In order to do this it is necessary to:
#     - hold the vertex id of the current node
#     - then look up the element number that matches the current node vertex id of the previous node
# In other words the column_id (element number) that matches the previous address_id will hold the distance from the
# current_address to the previous_address.
# // used for quick access to each address in the distance graph
# // if col is empty then replace with row[0] count
# * *************************************************************** *
# *                                                                 *
# * *************************************************************** *
# ------------------------------------------------------------------------------------------------------------------------
# |BIG O       |                                           PSEUDOCODE                                                    |
# ------------------------------------------------------------------------------------------------------------------------
# >>> initialize counter for vertex ids
#     >>> use for creating symmetrical graph
#     >>> if col is empty then replace with row[0] -> count
# >>> build undirected adjacency list
#         >>> start first level FOR loop
# O(N)........FOR EACH row IN LIST distances:
#             >>> fix last element form empty space to null space (' ' -> '')
#                 SET row[-1] = ''
#             >>> set the empty values in each row to the correct weight
# O((N)(5N))      FOR EACH column IN row:
#                     IF column = ''
#                     >>> get the row id
#                         u = row[0]
#                     >>> get and set weight from node a to node b
#                         INITIALIZE AND SET STRING a_to_b = STRING distances[i-1][u]
#                         IF a_to_b is not '':
#                         >>> set current vertex in node to the correct weight
#                             SET STRING row[i] = a_to_b
#                         ELSE:
#                         >>> set element to 0.0
#                         STRING row[i] = STRING '0.0'
#
#                         END IF/ELSE
#                     END IF
#                 END FOR
# O(N^2)       END FOR
#         >>>>start first level FOR loop
#         >>> convert all columns to float
#             INITIALIZE AND SET COUNTERS i, j = 0
#
# O(N+2)      FOR EACH row IN distances:
# O(N+2)(N)       FOR EACH column IN row:
#                 >>> convert current column to float
#                     SET distances[i][j] = float(column)
#                     INCREMENT COUNTER j BY 1
#                 END FOR
#
#                 SET COUNTER j = 0
#                 INCREMENT COUNTER i BY 1
#             >>> delete vertex_id, location_id is assumed to be row_id
#                 DELETE row[0]
# O(N^2)      END FOR
#
#             * ************************************************* *
#             * LIST distance now has the format:                 *
#             *                                                   *
#             * from_current_location_to_hub = row[1]             *
#             * from_current_location_to_location_1 = row[2]      *
#             * ....                                              *
#             * from_current_location_to_location_N = row[N+1]    *
#             * ************************************************* *
#
#             RETURN distances
# ------------------------------------------------------------------------------------------------------------------------
# BIG O TOTAL
# ------------------------------------------------------------------------------------------------------------------------
# O(N^2)
# """
#
#
# def build_adjacency_matrix():
#     """
#     :return: distances as adjacency list
#     """
#     for row in distances:
#         # fix last element from ' ' to ''
#         row[0] = ''
#         for i, col in enumerate(row):
#             if col == '':
#                 # get hash id for row
#                 u = row[0]
#                 # set col to weight from distance A -> B
#                 a_to_b = distances[i][u]
#                 if a_to_b != '':
#                     row[i] = a_to_b
#                 else:
#                     # set last element of last node to '0.0'
#                     row[i] = '0.0'
#
#     # convert all elements from string to float
#     i = 0
#     j = 0
#     for row in distances:
#         for col in row:
#             distances[i][j] = float(col)
#             j += 1
#         j = 0
#         i += 1
#
#         # remove vertex_id, location_id is assumed to be row_id
#         del row[0]
#     return distances
#
#     # convert all elements from string to float
#     i = 0
#     j = 0
#     for row in distances:
#         for col in row:
#             distances[i][j] = float(col)
#             j += 1
#         j = 0
#         i += 1
#         print(row)
#     return distances
#
#
# """
# FUNCTION sorted_adjacency_matrix
# The purpose of this function is to build a presorted adjacency matrix from distances in the format:
#     row[0] = [TUPLE(self_id, 0.0), TUPLE(closest_neighbor_id, miles_from_0_to_closest)....
#               furthest_neigbor_id, miles_from_0_to_furthest)],
#     row[1] = [TUPLE(self_id, 0.0), TUPLE(closest_neighbor_id, miles_from_1_to_closest)....
#               furthest_neigbor_id, miles_from_1_to_furthest)],
#     ... for all rows
#
# ------------------------------------------------------------------------------------------------------------------------
# BIG O       |                                           PSEUDOCODE                                                     |
# ------------------------------------------------------------------------------------------------------------------------
# With this format the rows are presorted for their closest neighbors and location_ids are easily accessible for the
# package and truck classes to access.
#             >>> clear each row of it's vertex_id
#             INITIALIZE AND SET LIST distances_only_table = distances[1:]
#
#             >>>>> first level for loop
# O(N + K)    FOR EACH row IN LIST distances_only_table
#                 DELETE first three elements
#                 DELETE t[0]
#                 DELETE t[0]
#                 DELETE t[0]
#             END FOR
#
#             SET AND INITIALIZE EMPTY LIST new_dist_graph
#
#             * *************************************************************** *
#             * u = row index                                                   *
#             * v = column index                                                *
#             * u and v are used instead of enumerate because they save one     *
#             * extra pass through the list that enumerate would have to do     *
#             * *************************************************************** *
#             SET AND INITIALIZE COUNTERS u, v = 0
#
#             >>> start first level FOR loop
# O(N+3)      FOR EACH row IN LIST distances_only_table
# O(N+3)(N)       FOR EACH column IN distances_only_table[u]
#                     IF column IS EMPTY
#                     >>> find the corresponding row to build bidirectional graph
#                     >>> offset d[v] by negative one for zero based indexing
#                         SET row[v-1] = TUPLE (v-1, float(dist_tbl_hash[v][u]))
#                     ELSE:
#                         SET row[v-1] = TUPLE (v-1, float(row[v-1]))
#
#                     INCREMENT v BY 1
#                 SET v = 1
#                 INCREMENT u BY 1
#
#             >>> sort the row in ascending order according to weight
#             * *************************************************************** *
#             * https://stackoverflow.com/questions/34830661/using-a-lambda-as\ *
#             * -key-within-builtin-string-sort-hard-to-identify-big-o          *
#             * *************************************************************** *
#             >>> O(NlogN)
#                 row.sort(key=lambda x: x[1])
#                 APPEND row TO LIST new_dist_graph
#             END FOR
#     >>> return new_dist_graph => sorted adjacency graph in ascending order by mileage
#     >>> LIST [(loc_id, mileage)...]
#         * *************************************************************** *
#         * new_dist_graph returns:                                         *
#         *     node N = [                                                  *
#         *     (N, 0.0), (closest_neighbor_M, miles_to_get_to_M)           *
#         *    …                                                            *
#         *     (furthest_neighbor_M, miles_to_get_to_M)                    *
#         *     ]                                                           *
#         * *************************************************************** *
#
#         RETURN new_dist_graph
# ------------------------------------------------------------------------------------------------------------------------
# BIG O TOTAL
# ------------------------------------------------------------------------------------------------------------------------
# O(N^2)
# """
#
#
# def sorted_adjacecny_matrix():
#     """
#     :return: distances as adjacency list in ascending order by mileage (nearest neighbor)
#     """
#     distances_only_table = dist_tbl_hash[1:]
#     # O(N)
#     for t in distances_only_table:
#         del t[0]
#         del t[0]
#         del t[0]
#
#     # create new distance graph
#     new_dist_graph = []
#     # u = row index
#     # v = 1 => column index, 1 to skip the first column which is already set in each vertex
#     u = 0
#     v = 0
#
#     for d in distances_only_table:
#         # v = column index
#         for e in distances_only_table[u]:
#             if e == '':
#                 #  find corresponding value in row to build bidirectional graph
#                 # offset d[v] by negative one for zero based indexing
#                 d[v] = (
#                 v - 1, float(dist_tbl_hash[v][u]))  # subtract 2 from v and add 2 to u to correct for skipped lines
#             else:
#                 d[v] = (v, float(d[v]))
#             v += 1
#         v = 1
#         u += 1
#         # O(NlogN)
#         d.sort(key=lambda x: x[1])
#         new_dist_graph.append(d)
#     # row[N] = [(N, 0.0), (closest_neighbor_id, miles_to_closest)...(furthest_neighbor_id, miles_to_furthest)]
#     return new_dist_graph
#
#
# """
# CLASS GRAPH
# DATA MEMBERS
# adjacency_list = build_adjacency_matrix()
# sorted_bidirectional_matrix()
# address_list = address_hash
# """
#
#
# class Graph:
#     """  Graph formats the distance data in dist_tbl_graph into bidirectional graphs  """
#
#     def __init__(self):
#         # O(N^2)
#         self.adjacency_list = build_adjacency_matrix()
#         # O(N^2)
#         self.sorted_bidirectional = sorted_adjacecny_matrix()
#         # O(1)
#         self.address_list = address_hash
#
#
# g = Graph()

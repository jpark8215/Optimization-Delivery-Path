#
# # Dijkstra shortest path - START
# class Vertex:
#     # Constructor for a new Vertx object. All vertex objects
#     # start with a distance of positive infinity.
#     def __init__(self, label):
#         self.label = label
#         self.distance = float('inf')
#         self.pred_vertex = None
#
#
# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}  # vertex dictionary {key:value}
#         self.edge_weights = {}  # edge dictionary {key:value}
#
#     def add_vertex(self, new_vertex):
#         self.adjacency_list[new_vertex] = []  # {vertex_1: [], vertex_2: [], ...}
#
#     def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
#         self.edge_weights[(from_vertex, to_vertex)] = weight
#         # {(vertex_1,vertex_2): 484, (vertex_1,vertex_3): 626, (vertex_2,vertex_6): 1306, ...}
#         self.adjacency_list[from_vertex].append(to_vertex)
#         # {vertex_1: [vertex_2, vertex_3], vertex_2: [vertex_6], ...}
#
#     def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
#         self.add_directed_edge(vertex_a, vertex_b, weight)
#         self.add_directed_edge(vertex_b, vertex_a, weight)
#
#
# # Dijkstra shortest path
# def dijkstra_shortest_path(g, start_vertex):
#     # Put all vertices in an unvisited queue.
#     unvisited_queue = []
#
#     for current_vertex in g.adjacency_list:
#         unvisited_queue.append(current_vertex)
#         # unvisited_queue = [vertex_1, vertex_2, ...]
#
#     # Start_vertex has a distance of 0 from itself
#     start_vertex.distance = 0
#
#     # One vertex is removed with each iteration; repeat until the list is
#     # empty.
#     while len(unvisited_queue) > 0:
#
#         # Visit vertex with minimum distance from start_vertex
#         smallest_index = 0
#         for i in range(1, len(unvisited_queue)):
#             # print(unvisited_queue[i].label, unvisited_queue[i].distance, unvisited_queue[i].pred_vertex)
#             if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
#                 smallest_index = i
#         current_vertex = unvisited_queue.pop(smallest_index)
#         # print("From Start Vetex to current_vertex.label: " + current_vertex.label +" distance: " + str(current_vertex.distance))
#
#         # Check potential path lengths from the current vertex to all neighbors.
#         for adj_vertex in g.adjacency_list[current_vertex]:  # values from  dictionary
#             # if current_vertex = vertex_1 => adj_vertex in [vertex_2, vertex_3], if vertex_2 => adj_vertex in [vertex_6], ...
#             edge_weight = g.edge_weights[(current_vertex, adj_vertex)]  # values from dictionary
#             # edge_weight = 484 then 626 then 1306, ...}
#             alternative_path_distance = current_vertex.distance + edge_weight
#
#             # If shorter path from start_vertex to adj_vertex is found, update adj_vertex's distance and predecessor
#             if alternative_path_distance < adj_vertex.distance:
#                 adj_vertex.distance = alternative_path_distance
#                 adj_vertex.pred_vertex = current_vertex
#
#
# def get_shortest_path(start_vertex, end_vertex):
#     # Start from end_vertex and build the path backwards.
#     path = ""
#     current_vertex = end_vertex
#     while current_vertex is not start_vertex:
#         path = " -> " + str(current_vertex.label) + path
#         current_vertex = current_vertex.pred_vertex
#     path = start_vertex.label + path
#     return path
#
#
# def get_shortest_path_city(start_vertex, end_vertex):
#     # Start from end_vertex and build the path backwards.
#     path = ""
#     current_vertex = end_vertex
#     while current_vertex is not start_vertex:
#         myMovie = myHash.search(int(current_vertex.label))
#         path = " -> " + myMovie.city + path
#         current_vertex = current_vertex.pred_vertex
#     path = "Salt Lake City " + path
#     return path
#
#
# # Dijkstra shortest path main
# # Program to find shortest paths from vertex A.
# g = Graph()
#
# # add Vertices
# vertex_1 = Vertex("1")  # 1, "CITIZEN KANE", 1941, 25.00, Salt Lake City, Utah
# g.add_vertex(vertex_1)
# vertex_2 = Vertex("2")  # 2, "CASABLANCA", 1942, 25.00, Helena, Montana
# g.add_vertex(vertex_2)
# vertex_3 = Vertex("3")  # 3, "THE GODFATHER", 1972, 10.00, Santa Fe, New Mexico
# g.add_vertex(vertex_3)
# vertex_4 = Vertex("4")  # 4, "GONE WITH THE WIND", 1939, 10.00, Austin, Texas
# g.add_vertex(vertex_4)
# vertex_5 = Vertex("5")  # 5, "LAWRENCE OF ARABIA", 1962, 10.00, Lincoln, Nebraska
# g.add_vertex(vertex_5)
# vertex_6 = Vertex("6")  # 6, "THE WIZARD OF OZ", 1939, 10.00, Madison, Wisconsin
# g.add_vertex(vertex_6)
# vertex_7 = Vertex("7")  # 7, "THE GRADUATE", 1967, 5.00, New York, New York
# g.add_vertex(vertex_7)
# vertex_8 = Vertex("8")  # 8, "ON THE WATERFRONT", 1954, 5.00, Columbus, Ohio
# g.add_vertex(vertex_8)
# vertex_9 = Vertex("9")  # 9, "SCHINDLER'S LIST", 1993, 5.00, Raleigh, North Carolina
# g.add_vertex(vertex_9)
# vertex_10 = Vertex("10")  # 10, "SINGIN' IN THE RAIN", 1952, 5.00, Orlando, Florida
# g.add_vertex(vertex_10)
# vertex_11 = Vertex("11")  # 11, "STAR WARS", 1977, 1.00, Montgomery, Alabama
# g.add_vertex(vertex_11)
#
# # add Edges
# g.add_undirected_edge(vertex_1, vertex_2, 484)  # 484 miles
# g.add_undirected_edge(vertex_1, vertex_3, 626)
# g.add_undirected_edge(vertex_2, vertex_6, 1306)
# g.add_undirected_edge(vertex_3, vertex_5, 774)
# g.add_undirected_edge(vertex_3, vertex_4, 687)
# g.add_undirected_edge(vertex_4, vertex_11, 797)
# g.add_undirected_edge(vertex_5, vertex_6, 482)
# g.add_undirected_edge(vertex_6, vertex_7, 936)
# g.add_undirected_edge(vertex_7, vertex_8, 535)
# g.add_undirected_edge(vertex_7, vertex_9, 504)
# g.add_undirected_edge(vertex_9, vertex_10, 594)
# g.add_undirected_edge(vertex_11, vertex_5, 970)
# g.add_undirected_edge(vertex_11, vertex_8, 664)
# g.add_undirected_edge(vertex_11, vertex_9, 567)
# g.add_undirected_edge(vertex_11, vertex_10, 453)
#
# # Run Dijkstra's algorithm first.
# dijkstra_shortest_path(g, vertex_1)
#
# # Get the vertices by the label for convenience; display shortest path for each vertex
# # from vertex_1.
# print("\nDijkstra shortest path:")
# for v in g.adjacency_list:
#     if v.pred_vertex is None and v is not vertex_1:
#         print("1 to %s ==> no path exists" % v.label)
#     else:
#         print("1 to %s ==> %s (total distance: %g)" % (v.label, get_shortest_path(vertex_1, v), v.distance))
#
# print("\nDijkstra shortest path with Cities:")
# for v in g.adjacency_list:
#     myMovie = myHash.search(int(v.label))
#     if v.pred_vertex is None and v is not vertex_1:
#         print("Salt Lake City to %s ==> no path exists" % myMovie.city)
#     else:
#         print("Salt Lake City to %s ==> %s (total distance: %g)" % (
#         myMovie.city, get_shortest_path_city(vertex_1, v), v.distance))
# # Dijkstra shortest path - END

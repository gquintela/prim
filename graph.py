class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.size = 0

    def get_vertices(self):
        output = []
        for vertex in self.adjacency_list:
            output.append(vertex)
        return output

    def get_neighbours(self, v):
        list = []
        for neighbour in self.adjacency_list[v]:
            list.append(neighbour)
        return list

    def print_vertices(self):
        print ("Vertices:")
        for vertex in self.adjacency_list:
            print(vertex)
        print('\n')

    def print_neighbours(self, v):
        print ("Neighbours of " + v)
        for neighbour in self.adjacency_list[v]:
            print (neighbour[0] + ", weight of edge: " + str(neighbour[1]))

    # v is not in the graph
    def add_vertex(self, v):
        self.adjacency_list[v] = []

    def add_undirected_edge(self, u, v, w):
        if u not in self.adjacency_list:
            self.add_vertex(u)
        if v not in self.adjacency_list:
            self.add_vertex(v)
        self.adjacency_list[u].append([v, w])

    def add_directed_edge(self, u, v, w):
        self.add_undirected_edge(u, v, w)
        self.add_undirected_edge(v, u, w)
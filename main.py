from algorithm import *

# create dummy graph & driver test
my_graph = Graph()
my_graph.add_directed_edge('r', 's', 5)
my_graph.add_directed_edge('t', 'u', 3)
my_graph.add_directed_edge('w', 'x', 2)
my_graph.add_directed_edge('x', 'y', 4)
my_graph.add_directed_edge('r', 'v', 8)
my_graph.add_directed_edge('s', 'w', 9)
my_graph.add_directed_edge('t', 'x', 1)
my_graph.add_directed_edge('u', 'y', 2)
my_graph.add_directed_edge('t', 'w', 6)
my_graph.add_directed_edge('u', 'x', 2)
my_graph.add_directed_edge('a', 'b', 9)
my_graph.add_vertex('z')

my_graph.print_neighbours('r')
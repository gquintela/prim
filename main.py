from algorithm import *

# create dummy graph & driver test
my_graph = Graph()
my_graph.add_directed_edge('a', 'b', 4)
my_graph.add_directed_edge('a', 'h', 8)
my_graph.add_directed_edge('b', 'c', 8)
my_graph.add_directed_edge('c', 'd', 7)
my_graph.add_directed_edge('b', 'h', 11)
my_graph.add_directed_edge('h', 'i', 7)
my_graph.add_directed_edge('i', 'c', 2)
my_graph.add_directed_edge('i', 'g', 6)
my_graph.add_directed_edge('h', 'g', 1)
my_graph.add_directed_edge('g', 'f', 2)
my_graph.add_directed_edge('c', 'f', 4)
my_graph.add_directed_edge('d', 'f', 14)
my_graph.add_directed_edge('d', 'e', 9)
my_graph.add_directed_edge('f', 'e', 10)

tree = prim(my_graph, 'a')




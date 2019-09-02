from graph import *
from heapq import *

infinite = 99999

    #v is contained in graph
def prim(graph: Graph, v):
    output = []
    parent = {}
    vertices_seen = {}
    queue = []
    for vertex in graph.get_vertices():
        parent[vertex] = None
        vertices_seen[vertex] = False
        heappush(queue, (infinite, vertex))
    heappush(queue, (0, v))
    counter = len(vertices_seen)
    while counter != 0:
        u = heappop(queue)
        if not vertices_seen[u[1]]:
            counter = counter - 1
            output.append(u[1])
            vertices_seen[u[1]] = True
            for neighbour in graph.get_neighbours(u[1]):
                if not vertices_seen[neighbour[0]]:
                    heappush(queue, (graph.get_weight(u[1], neighbour[0]) , neighbour[0]))
                    parent[neighbour[0]] = u[1]
    print('mst-tree created with Prim\'s algorithm rooted in vertex \'' + v + '\':')
    print (parent)
    return parent


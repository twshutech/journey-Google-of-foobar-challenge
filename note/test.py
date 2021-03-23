import networkx as nx
import matplotlib.pyplot as plt
import random

G=nx.Graph(name="buba")
routes = [[2, 1, 4, 3, 11], [1, 0, 3, 11, 10], [10, 11, 3, 4, 1]]
edges = []
for r in routes:
    route_edges = [(r[n],r[n+1]) for n in range(len(r)-1)]
    G.add_nodes_from(r)
    G.add_edges_from(route_edges)
    edges.append(route_edges)

print("Graph has %d nodes with %d edges" %(G.number_of_nodes(),
G.number_of_edges()))

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos=pos)
nx.draw_networkx_labels(G,pos=pos)
colors = ['r', 'b', 'y']
linewidths = [20,10,5]
for ctr, edgelist in enumerate(edges):
    nx.draw_networkx_edges(G,pos=pos,edgelist=edgelist,edge_color = colors[ctr], width=linewidths[ctr])
plt.savefig('this.png')
